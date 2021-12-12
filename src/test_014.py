#Typos and Find the same text in a webpage
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
#from selenium.webdriver.common.by import By 
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from time import sleep


class Typos(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
        driver= self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Typos").click()
    #End of setUp

    #Test Cases
    #This case checks if the given text is equal to the one corresponding to the web page. 
    def test_name_elements(self):
        driver = self.driver
        
        #Finds the chosen text and then it converts it into plain text.
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        #variables
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        #If the text is different to the text which is intended to be found, refresh the web page.
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
            text_to_check = paragraph_to_check.text
            driver.refresh
        
        #While the text is not found, the variables will change, until found change from False to True
        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True
        
        #Verifies that found is equal to True
        self.assertEqual(found, True)

        #Console output
        print(f"It took {tries} tries to find the typo.")
    #End of test_name_elements

    #Close
    def tearDown(self):
        self.driver.close()
    #End of tearDown

#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)