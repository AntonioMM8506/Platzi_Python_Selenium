#Handling dropdown menues and lists
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
#submodule for handling drop-down menues
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
	#End of setUp
	
	def test_select_language(self):
		exposed_options = ['English', 'French', 'German']
		#to store the options to select
		active_options = []
		#to access to the options of the dropdown menu
		select_language= Select(self.driver.find_element_by_id('select-language'))
		#to validate that the quantity of options are the same as the expected
		#'options' allows to access directly to the options of the dropdown menu
		self.assertEqual(3, len(select_language.options))

		for option in select_language.options:
			active_options.append(option.text)
		
		#Verifies that the list of available options and the active ones are the same
		self.assertListEqual(exposed_options,active_options)

		#Verifies that the first option is "English" in the dropdown menu
		self.assertEqual('English', select_language.first_selected_option.text)

		#It selects the option with the text "German"
		select_language.select_by_visible_text('German')

		#Verifies if the page is translated to German
		#Verifies that the url contains the words
		self.assertTrue('store=german' in self.driver.current_url)

		select_language= Select(self.driver.find_element_by_id('select-language'))
		select_language.select_by_index(0)
	#End of test_select_language

	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()
	#End of tearDown

#MAIN
if __name__ == "__main__":
	unittest.main(verbosity = 2)
