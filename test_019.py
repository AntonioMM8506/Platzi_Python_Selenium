import unittest 
from selenium import webdriver
from time import sleep

#Tehcnical Test
class TestingMercadoLibre(unittest.TestCase):

    #Initialization
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:/Users/ASUS/Documents/VS Code/JavaScript/Platzi/Selenium/chromedriver.exe')
        driver= self.driver
        #driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.mercadolibre.com")

    #
    #
    #
    def test_search(self):
        driver = self.driver
        country = driver.find_element_by_id('CO')
        country.click()

        search_field =driver.find_element_by_name("as_word")
        search_field.click()
        search_field.clear()
        search_field.send_keys("PlayStation 4")
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text("Bogotá D.C.")
        #location.click()
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element_by_partial_link_text("Nuevo")
        #condition.click()
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element_by_class_name('ui-dropdown__link')
        order_menu.click()

        higher_price = driver.find_element_by_css_selector('#inner-main > aside > section.view-options > dl > div > div > div > div > ul > li.ui-list__item.ui-list__item--selected > span')
        #higher_price.click()
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div[2]/div/h2/a/span').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div[2]/div/div[1]/div/span[2]').text
            prices.append(article_price)

        print(articles, prices)


    #Close
    def tearDown(self):
        self.driver.close()


#MAIN
if __name__== '__main__':
    unittest.main(verbosity=2)