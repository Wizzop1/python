from distutils.filelist import findall
from msilib.schema import ServiceControl
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import pandas as pd
ser = Service()
ser.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
products = []
prices = []
ratings = []
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.find_all('a', href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    rating.append(rating.text)
dictProducts = {'Product Name':products,'Price':prices,'Rating':ratings}
df = pd.DataFrame.from_dict(dictProducts, orient='index')
df.to_csv('products.csv', index=False, encoding='utf-8')