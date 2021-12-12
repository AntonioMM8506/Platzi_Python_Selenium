#Find Elements
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver


class HomePageTests(unittest.TestCase):

    #Executes before the tests
    def setUp(self):
        self.driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        #Expands the window in order to fulfill the whole screen.
        driver.maximize_window()
        driver.implicitly_wait(20)
    #End of setUp

    #Searches using the id of a tag
    def test_serach_text_field(self):
        search_field = self.driver.find_element_by_id("search")
    #End of test_search_text_field

    #Searches using the name of a tag
    def test_search_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")
    #End of test_search_field_by_name

    #Searches using the name of the tag
    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")
    #End of test_searcg_text_field_class_name

    #Searches using the class of the tag
    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button") 
    #End of test_search_button_enabled   

    #Searches in a list of various elements such is a list
    #First looks after the class names and then after the tag names
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))
    #End of test_count_of_promo_banner_images

    #Searches using the xpath of the tag. This is given by selecting a special
    #type of copy command. 
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[1]/a')
    #End of test_vip_promo

    #Searches using the composition of tags of a css file/tag
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
    #End of test_shopping_cart

    #Executes after
    def tearDown(self):
        self.driver.quit()
    #End of tearDown

#MAIN
if __name__ == "__main__":
    unittest.main(verbosity=2)
