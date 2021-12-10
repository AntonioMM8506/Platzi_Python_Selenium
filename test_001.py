#Introduction to Selenium

#Import modules for testing
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

#We use a class in order to manage objects
class HelloWorld(unittest.TestCase):
    
    #Overrides the function in order to work it as a class. Calling the Chrome driver with its pad
    #Then, it waits a short period of time in order to start the test.
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(20)

    #It calls the given url so the explorer can open and access to it. 
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www3.animeflv.net/ver/noragami-aragoto-3')

    #Same function as before but simplified
    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    #WIth this override, using the function to work with the class, it can open an closes the explorer
    #in one single iteration. 
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

#Main function. the function HTMLTestRUnner generates a report in the directory output and with the name
#of report_name, This is saved in a HTML format.
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner = HTMLTestRunner(output = "reportes", report_name ="hello-world-report"))
