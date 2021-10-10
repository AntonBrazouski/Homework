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
data_dict = {}
for each_item in items:
    item = str(each_item)
    
    title = re.findall(r'<title>(.*?)</title>', str(each_item))[0]
    

    link = re.findall(r'<link>(.*?)</link>', item)[0]
    pub_date = re.findall(r'<pubDate>(.*?)</pubDate>', item)[0]
    data_dict['title'] = title
    data_dict['link'] = link 
    data_dict['pub_date'] = pub_date

    data.append(data_dict)
    #print(data_dict)
    data_dict = {}

print(data[0:2])
for item in data:
    print(item)