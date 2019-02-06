import requests
from bs4 import BeautifulSoup
class site():
    def __init__(self, addr, ta):
        self.address = addr
        self.tag = ta

    def tm(self):
        response = requests.get(self.address)
        t = BeautifulSoup(response.text, "html.parser")
        tem = t.select(self.tag)
        print(tem[0].text)


k = '.today-temp'
page = "https://sinoptik.ua/погода-киев"
a = site(page, k)
a.tm()
