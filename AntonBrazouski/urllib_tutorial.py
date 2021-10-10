import urllib.request

request_url = urllib.request.urlopen('https://news.yahoo.com/rss/')

print(request_url.read())

