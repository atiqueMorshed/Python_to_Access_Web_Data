import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
page = urllib.request.urlopen(url).read()
parsed = BeautifulSoup(page, 'html.parser')
numbers = parsed('span')
sum = 0
for val in numbers:
    sum += int(val.contents[0])

print(sum)