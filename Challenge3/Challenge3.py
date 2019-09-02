import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        popular_array = self.driver.find_elements_by_xpath('//div[@ng-if="popularSearches"]//ul/li/a')
        for x in popular_array:
           print(x.get_property('text'), x.get_attribute('href'))

if __name__ == '__main__':
    unittest.main()

