import requests
from bs4 import BeautifulSoup

page = "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2"

response = requests.get(page)
soup = BeautifulSoup(response.text, 'html.parser')
weather = soup.find	(id="today-temp")
#weather = soup.select(".today-temp")
print(weather[0].text)