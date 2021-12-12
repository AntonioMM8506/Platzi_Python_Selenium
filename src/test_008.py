#Handling alerts and pop-ups
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver


class CompareProducts(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
	#End of setUp
	
	def test_compare_products_removal_alert(self):
		driver = self.driver
		search_field = driver.find_element_by_name('q')
		#As a good practice it is recommended to clear the fields
		search_field.clear()

		search_field.send_keys('tee')
		search_field.submit()

		driver.find_element_by_class_name('link-compare').click()
		driver.find_element_by_link_text('Clear All').click()
		
		#creates a variable to interact with the pop-up window
		alert = driver.switch_to_alert()
		#extracts the text that this alert contains
		alert_text = alert.text
        
		#Verifies the text of the alert
		self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
		
		alert.accept()
	#End of test_compare_products_removal_alert

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()
	#End of tearDown

#MAIN
if __name__ == "__main__":
	unittest.main(verbosity = 2)
