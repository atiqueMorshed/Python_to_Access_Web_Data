import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input("URL: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_413800.xml"
print("Retrieving", url)
xml = urllib.request.urlopen(url).read()
print("Retrieved", len(xml), "characters")
tree = ET.fromstring(xml)
counts = tree.findall(".//count")
print("Count:", len(counts))
total = 0
for count in counts:
    total += int(count.text)
print("Sum:", total)
