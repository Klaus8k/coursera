import urllib.parse as urlpars
import html
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup

url = 'https://my.offerrum.com/offers/all?categories=47%2C12%2C14%' \
      '2C18%2C45%2C23%2C15%2C42%2C22%2C20%2C52%2C16%2C40%2C21%2' \
      'C19%2C17%2C53%2C49%2C46%2C54%2C50%2C94%2C51%2C55%2C57%2C56%2C1' \
      '&countries=RU&limit=All&page=0&pixelGroups=5&sortBy=&sortOrder=&tab=all'

# file = r'C:\Users\Copy\Desktop\Офферы.mhtml'


class MyParce(HTMLParser):
    def __init__(self):
        super(MyParce, self).__init__()
        self.reset()
        self.result = []

    def handle_starttag(self, tag, attrs):
        if attrs:
            if tag == 'a' and 'class="offer-title"' in attrs[0] :
                self.result.append(attrs)

def connect(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.3.848 Yowser/2.5 Safari/537.36',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'

    }
    r = requests.get(url, headers= headers)
    responce = r.text
    responce.encode('utf-8')
    return responce

def write_to_file(data):
    with open('2.txt', 'w') as file:
        file.write(data)


responce = connect(url)
write_to_file(responce)
soup = BeautifulSoup(responce, 'html.parser')
print(soup)


# site = MyParce()
# site.feed(x)
#
# print(site.result)