import urllib.request
import urllib.parse
import re

url = 'https://news.yahoo.com/rss/'
# values = {'s': '<item>', 's2':'</item>'}

# data = urllib.parse.urlencode(values)
# print(type(data))
# print(data)
# data = data.encode('utf-8')
# print(type(data))
# req = urllib.request.Request(url, data)
# print(type(req))
# print(req)
# # resp = urllib.request.urlopen(req)


request_url = urllib.request.urlopen(url)

resp_data = request_url.read()
print(type(resp_data))

items = re.findall(r'<item>(.*?)</item>', str(resp_data))

data = []
for each_item in items:
    item = re.findall(r'<title>(.*?)</title>', str(each_item))
    data.append(item[0])

for item in data:
    print(item)