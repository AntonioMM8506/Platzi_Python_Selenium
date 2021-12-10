import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
#from selenium.webdriver.common.by import By 
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#DDT

#decorator
@ddt
class SearchDDT(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver= self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com")

    #With this, it can send the data to the following function automatically 
    # For example, search_value = dress, expected_count = 6     
    @data(("dress",6),("music",5))
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
        print(f"Found {len(products)} products")

        #The previous variable returns a list of the found elements, with this one can print it
        for product in products:
            print(product.text)
        
        #If the obtained values are the expected ones. 
        self.assertEqual(expected_count, len(products))

    #Close
    def tearDown(self):
        self.driver.close()


#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)