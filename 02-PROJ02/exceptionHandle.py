import urllib.request

try:
    webPage = urllib.request.urlopen('http://www.google.in')
except:
    print('The webPage is unreachable')
else:
    for line in webPage:
        print(line)