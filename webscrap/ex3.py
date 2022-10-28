from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
n = int(input())
for i in range(n):
    try:
        html = urlopen("https://ganbox.com/")
    except HTTPError as e:
        print('HTTP Error')
    except URLError as e:
        print('URL Error')
    else:
        print(html.read())
