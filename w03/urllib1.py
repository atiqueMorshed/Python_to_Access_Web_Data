import urllib.request, urllib.parse, urllib.error

handler = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
# OR
# handler = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for lines in handler:
    print(lines.decode().strip())
