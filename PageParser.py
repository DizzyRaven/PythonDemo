import requests
from bs4 import BeautifulSoup

class PageParser(object):
   def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

   def getTagValue(self,tag):
    soup = BeautifulSoup(self.response.text, 'html.parser')
    weather = soup.select(tag)
    return weather[0].text
        