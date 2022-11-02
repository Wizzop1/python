from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
driver = webdriver.Firefox(options=options)
driver.get("https://python.org")
time.sleep(3)
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
time.sleep(3)
elem.send_keys("pycon")
time.sleep(3)
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert "No Results found." not in driver.page_source 

driver.close()
