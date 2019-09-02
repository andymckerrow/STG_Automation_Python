import time
import unittest

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element_by_id('input-search').send_keys('exotics' + Keys.ENTER)
        self.assertIn('exotic', self.driver.title)
        table = self.driver.find_element_by_xpath('//table[@id="serverSideDataTable"]//tbody')
        table_text = table.get_attribute('innerText')
        assert 'PORSCHE' in table_text

if __name__ == '__main__':
    unittest.main()


#below is alternative to line 21. Makes it easier to change what you search for on the whole test, but longer
#searchterm = 'exotics'
#searchfield = self.driver.find_element_by_id('input-search')
#searchfield.send_keys(searchterm)
#searchfield.send_keys(Keys.Enter)

#below replaces 22 and 23 and includes the Wait to make sure it works every time but it requires importing "EC" at the top
#dataelement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id*\"serverSideDataTable\"]//tbody")))
#html = dataelement.get_attribute('innerHTML')
#self.assertIn('PORSCHE, html')

