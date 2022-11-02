from selenium import webdriver
from selenium.webdriver.common.by import By
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
driver = webdriver.Firefox(options=options)
driver.get(url="https://www.google.com/")  
driver.find_element(By.ID, 'W0wltc').send_keys(Keys.ENTER)
driver.find_element(By.NAME, "q").send_keys("youtube")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME, 'btnK').click()
time.sleep(3)  
driver.close()