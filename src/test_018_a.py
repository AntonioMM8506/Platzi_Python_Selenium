#POM - Page Object Model
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
from time import sleep
from test_018_b import GooglePage


class GoogleTest(unittest.TestCase):

    #Initialization
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
    #End of setUp

    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("GitHub")

        self.assertEqual("GitHub", google.keyword)
    #End of test_search

    #Close
    @classmethod
    def tearDown(cls):
        cls.driver.close()
    #End of tearDown

#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)
