from pickletools import pystring
#find all strings containing python in them
import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs= requests.get(url)
soup = BeautifulSoup(reqs.text , 'html.parser')
pyStrings = soup.find_all(string = re.compile('Python'))
for txt in pyStrings:
    print(' '.join(txt.split()))