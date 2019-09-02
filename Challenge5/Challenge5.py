import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

 #   def tearDown(self):
  #      self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.driver.find_element_by_id('input-search').send_keys('porsche' + Keys.ENTER)
       # self.driver.find_element_by_name('serverSideDataTable_length').send_keys('100' + Keys.ENTER)
        self.driver.find_element_by_xpath('//*[@id="serverSideDataTable_length"]/label').click()
        self.driver.find_element_by_xpath('//*[@id="serverSideDataTable_length"]/label/select/option[3]').click()

        time.sleep(10)



if __name__ == '__main__':
    unittest.main()
