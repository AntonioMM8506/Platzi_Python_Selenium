#Add and Remove elements on the website
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
from time import sleep


class AddRemoveElements(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Add/Remove Elements").click()
    #End of setUp

    #Test cases
    def test_add_remove(self):
        driver = self.driver
        #Console inputs
        elements_added = int(input("How many elements will you add?: "))
        elements_removed = int(input("How many elements will you remove?: "))
        total_elements = elements_added - elements_removed
        
        #Finds the element of the button by its xpath
        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        
        #Waits for 3 seconds
        sleep(3) 

        #Adds the button with a for loop
        for i in range(elements_added):
            add_button.click()
        
        #Removes the elements with a for loop, but it also contains a try-catch in case the given number
        #of deleted elements exceed the added ones. 
        for j in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print("You're trying to delete more elements than the existent")
                break
        
        #Console output messages. 
        if total_elements > 0:
            print(f"there are {total_elements} elements on the screen")
        else:
            print("There are 0 elements on the screen")

        sleep(3)
    #End of test_add_remove

    #Close driver
    def tearDown(self):
        self.driver.close()
    #End of tearDown

#MAIN
if __name__ == "__main__":
	unittest.main(verbosity = 2)
