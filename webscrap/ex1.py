from bs4 import BeautifulSoup
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

ser = Service()
p = []
ser.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://ganbox.com")
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.find_all('p'):
        para=a.find('p')
        p.append(para)
print(p)
driver.close()