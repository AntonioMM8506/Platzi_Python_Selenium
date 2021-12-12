#Handling Forms, Textboxes and Radio Buttons
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo.onestepcheckout.com/")
	#End of setUp
	
	def test_new_user(self):
		driver = self.driver
		#Finds the element by xpath and then clicks on it to deploy the menu
		driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
		#Finds the element by its text and then clicks on it
		driver.find_element_by_link_text('Log In').click()
		#Creates a variable associated to clicking on the element
		create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
		
		#Validates that the button is visible and clickable
		self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
		create_account_button.click()

		#Verifies that the context/page is the given one
		self.assertEqual('Create New Customer Account', driver.title)

		#variables corresponding with the elements
		first_name = driver.find_element_by_id('firstname')
		last_name = driver.find_element_by_id('lastname')
		email_address = driver.find_element_by_id('email_address')
		password = driver.find_element_by_id('password')
		confirm_password = driver.find_element_by_id('confirmation')
		news_letter_subscription = driver.find_element_by_id('is_subscribed')
		submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

		#Check if the elements are enabled
		self.assertTrue(first_name.is_enabled() 
		and last_name.is_enabled()
		and email_address.is_enabled()
		and password.is_enabled()
		and confirm_password.is_enabled()
		and news_letter_subscription.is_enabled()
		and submit_button.is_enabled())

		#Send the data to the Form
		first_name.send_keys('Test')
		last_name.send_keys('Test')
		email_address.send_keys('arqcftlothxuknlxkt@awdrt.com') #retrieved from 10-minute mail
		password.send_keys('Test')
		confirm_password.send_keys('Test')
		submit_button.click()
	#End of test_new_user

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()
	#End of tearDown

#MAIN
if __name__ == "__main__":
	unittest.main(verbosity = 2)
