#Find Elements

#Import modules for testing
import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    #Executes before the tests
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Expands the window in order to fulfill the whole screen.
        driver.maximize_window()
        driver.implicitly_wait(20)

    #Searches using the id of a tag
    def test_serach_text_field(self):
        search_field = self.driver.find_element_by_id("search")

    #Searches using the name of a tag
    def test_search_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    #Searches using the name of the tag
    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    #Searches using the class of the tag
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")    

    #Searches in a list of various elements such is a list
    #First looks after the class names and then after the tag names
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    #Searches using the xpath of the tag. This is given by selecting a special
    #type of copy command. 
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[1]/a')

    #Searches using the composition of tags of a css file/tag
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    #Executes after
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)