import sys
import requests
from bs4 import BeautifulSoup

class WebParser(object): #Зачем непосредственно необходим "object"
    def __init__(self, url):
        self.url = url
    def getsomeinf(self, tag):
        response = requests.get(self.url)
        html_text = BeautifulSoup(response.text, 'html.parser')
        today_temp = html_text.select(tag)
        print(today_temp[0].text)
        """for i in range(len(today_temp) - 1):
            print(today_temp[i].text)"""
        
print("Введите искомый адрес:")
page = sys.stdin.readline()#"https://sinoptik.ua/погода-киев"
print("Введите искомый тег:")
tag = sys.stdin.readline()#".today-temp"
td_wthr = WebParser(page)
td_wthr.getsomeinf(tag)
