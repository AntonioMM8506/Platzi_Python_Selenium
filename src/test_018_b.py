#POM - Project Object Model
#Import modules to read env files
import os
from dotenv import load_dotenv
load_dotenv()
#Import modules for testing
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from time import sleep


class GooglePage(object):

    def __init__(self, driver):
        self._driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_PATH'))
        self._url = "https://google.com"
        self.search_locator = "q"

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME,"q")))
        return True
    #End of is_loaded

    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name("q")
        return input_field.get_attribute("value")
    #End of keyword

    def open(self):
        self._driver.get(self._url)
    #End of open

    def type_search(self, keyword):
        input_field = self._driver.find_element_by_name("q")
        input_field.send_keys(keyword)
    #End of type_search

    def click_submit(self):
        input_field = self._driver.find_element_by_name("q")
        input_field.submit()
    #End of click_submit

    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit
    #End of search
