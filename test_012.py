import unittest
from selenium import webdriver
from time import sleep
#Dynamic Elements
#Disappearing Elements

class DynamicElements(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver= self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Disappearing Elements").click()

    #Test Cases
    #
    def test_name_elements(self):
        driver = self.driver

        options= []
        menu = 5
        tries = 1

        #While the lenght of the list is <5 just clean it.
        while len(options) < 5:
            options.clear()

            #With a for loop, iterates along the list of elements, if it found it, it appends it to the list
            for i in range(menu):
                try:
                    option_name= driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                except:
                    #When it overflows the list, it will triger this exception. 
                    print(f"Option number {i+1} is not found")
                    tries= tries +1
                    driver.refresh()
            
            print(f"Finished in {tries} tries")
    
    #Close
    def tearDown(self):
        self.driver.close()


#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)