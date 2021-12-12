#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
#It is useful when we require to validate the presence of an element
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")
	#End of setUp

	def test_search_field(self):
		self.assertTrue(self.is_element_present(By.NAME, 'q'))
	#End of test_search_field

	def test_language_option(self):
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))
	#End of test_language_option

	def tearDown(self):
		self.driver.quit()
	#End of tearDown

	#To know if the element is present
	#how: type of selector
	#what: the current value
	def	is_element_present(self, how, what):
		try:  #Search for the elements based on the value
			self.driver.find_element(by = how, value = what) 
		except NoSuchElementException as variable:
			return False
		return True
	#End of is_element_present

#MAIN
if __name__ == "__main__":
    unittest.main(verbosity=2)
