import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#Dynamic Elements
#Dynamic Controls

class DynamicElements(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver= self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Dynamic Controls").click()

    #Test Cases
    #This function will click the given button, ideintified by its css path, but it will wait until the element 
    #is visible. 
    def test_name_elements(self):
        driver = self.driver
        
        #Finds the checkbox element and then click it.
        #copy selector/css
        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()

        #Clicks the element twice, before the second time it waits for 15 seconds or until the element
        #is visible/clickable once again, this using the By Module.
        remove_add_buttom = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_buttom.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_buttom.click()
        
        #Similar to the previous case, but this time it will do it with an input/submit button, in order
        #to enable a textbox.
        enable_disable_buttom = driver.find_element_by_css_selector("#input-example > button")
        enable_disable_buttom.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button")))
        #In this case, it will send some raw data to the text field. 
        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.send_keys("Platzi")
        #disables the textbox once again.
        enable_disable_buttom.click()

    #Close
    def tearDown(self):
        self.driver.close()


#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)