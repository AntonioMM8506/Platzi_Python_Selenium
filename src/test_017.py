#DDT with CSV file
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest 
import csv
from selenium import webdriver
from ddt import ddt, data, unpack
#from selenium.webdriver.common.by import By 
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def get_data(file_name):
    rows = []
    data_file = open(file_name, "r")
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows

#decorator
@ddt
class SearchCCVDDT(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
        driver= self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")
    #End of setUp

    @data(*get_data("testdata.csv"))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        #It finds the text box, clears it and then send the values of the parameters
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #Finds the products by their xpath, this is a elementS_xpath
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')

        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name("note-smg")
            self.assertEqual("Your search returns no results", message)

        print(f"Found {len(products)} products")
    #End of test_search_ddt

    #Close
    def tearDown(self):
        self.driver.close()
    #End of tearDown

#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)
