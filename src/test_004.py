#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class SearchTests(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com")
	#End of setUp

	def test_search_tee(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		search_field.clear() #Cleans the textfield in case there's some previous data
		
		search_field.send_keys('tee') #inputs the value "tee" in the specified textbox
		search_field.submit() #Submit the data ('tee')
	#End of test_search_tee
		
	def test_search_salt_shaker(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		
		search_field.send_keys('salt shaker') #it writes 'salt shaker' in the searching bar
		search_field.submit() #it sends the petition

		#makes a list of the query searching the elements by their xpath
		products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

		#Compares if the number of results is equal to 1
		self.assertEqual(1, len(products))
	#End of test_search_salt_shaker
		
	def tearDown(self):
		self.driver.quit()
	#End of tearDown

#MAIN
if __name__ == "__main__":
    unittest.main(verbosity=2)
