import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("URL: ")
count = int(input("Count: "))
pos = int(input("Position: ")) - 1
page = urllib.request.urlopen(url).read()
parsed = BeautifulSoup(page, 'html.parser')
lists = parsed('a')
nextUrl = None
i = 0
posCount = 0
name = ""
print(url+"\n")
for i in range(count):
    if nextUrl is not None:
        page = urllib.request.urlopen(nextUrl).read()
        parsed = BeautifulSoup(page, 'html.parser')
        lists = parsed('a')
    for lst in lists:
        if posCount is not pos:
            posCount += 1
            continue
        name = lst.contents[0]
        print(lst.get('href', None))
        nextUrl = lst.get('href', None)
        posCount = 0
        break
print(name)
