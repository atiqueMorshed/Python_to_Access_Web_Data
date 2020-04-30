import json
import urllib.request, urllib.parse, urllib.error
count = 0

url = "http://py4e-data.dr-chuck.net/comments_413801.json"
print("retrieving URL. Stand by.")
opUrl = urllib.request.urlopen(url)
data= opUrl.read()

data = json.loads(data)
for item in data["comments"]:
    number = int(item["count"])
    count = count + number
print(count)
