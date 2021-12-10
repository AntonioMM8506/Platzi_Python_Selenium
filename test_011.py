import unittest
from selenium import webdriver
from time import sleep
#Add and remove elements on "The Internet" Website"

class AddRemoveElements(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element_by_link_text("Add/Remove Elements").click()

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

    #Close driver
    def tearDown(self):
        self.driver.close()

#Main ---------------------------------------------------------------------    
if __name__ == "__main__":
	unittest.main(verbosity = 2)