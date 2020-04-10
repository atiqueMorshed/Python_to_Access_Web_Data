import urllib.request, urllib.parse, urllib.error

container = dict()
handler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for lines in handler:
    words = lines.decode().split()
    for val in words:
        container[val] = container.get(val, 0) + 1
print(container)
