#Sleep/Pauses
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
from time import sleep


class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("https://www.google.com/")
	#End of setUp

	def test_browser_navigation(self):
		driver = self.driver

		search_field = driver.find_element_by_name('q')
		search_field.clear()
		search_field.send_keys('python')
		search_field.submit()

		driver.back()#goes back
		sleep(3) #waits for 3 seconds
		driver.forward() #goes forward
		sleep(3) 
		driver.refresh() #refresh page
		sleep(3)
	#End of test_browser_navigation


	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()
	#End of tearDown

#MAIN
if __name__ == "__main__":
	unittest.main(verbosity = 2)
