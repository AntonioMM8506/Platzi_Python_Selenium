import unittest
from selenium import webdriver
from time import sleep
from test_018_b import GooglePage

#POM - Page Object Model

class GoogleTest(unittest.TestCase):

    #Initialization
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')


    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search("Platzi")

        self.assertEqual("Platzi", google.keyword)


    #Close
    @classmethod
    def tearDown(cls):
        cls.driver.close()


#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)