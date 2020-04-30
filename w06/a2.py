import urllib.parse, urllib.error, urllib.request
import json
target = 'http://py4e-data.dr-chuck.net/json?'
plc = "University of Kerala"
url = target + urllib.parse.urlencode({'address': plc, 'key': 42})
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
print('Place id', js['results'][0]['place_id'])
