import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
class PythonSearch(unittest.TestCase):
    def setUp(self):    
        options = Options()
        options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
        driver = webdriver.Firefox(options=options)
    def test_search_in_python(self):
        driver = self.driver
        driver.get("https://python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, 'q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found", driver.page_source)

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()