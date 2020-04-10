import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
page = urllib.request.urlopen(url, context=ctx).read()
parsed = BeautifulSoup(page, 'html.parser')
tags = parsed('a')
print("\nhref: ")
for tag in tags:
    print(tag.get('href', None))
print("\nContents: ")
for tag in tags:
    print('Contents:', tag.contents[0])
print("\nAttributes: ")
for tag in tags:
    print('Attrs:', tag.attrs)
