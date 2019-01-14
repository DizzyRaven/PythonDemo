
from PageParser import PageParser

url = "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2"
tag = ".today-temp"

pageParser = PageParser(url)

weather = pageParser.getTagValue(tag)

print("Weather today is "+weather)



