import argparse
import urllib.request
import re


# argparse

parser = argparse.ArgumentParser(description='RSS Parser')
parser.add_argument('link', metavar='L', type=str,
                    help='link for rss feed')
parser.add_argument('--version', action='version', version='0.1',
                    help="Print version info")

parser.add_argument('-v', "--verbose", action='store_true',
                    help='Outputs verbose status messages')

args = parser.parse_args()

if args.verbose:
    print(f"parsing rss link: {args.link}")


# urllib
url = args.link

request_url = urllib.request.urlopen(url)

resp_data = request_url.read()
# print(type(resp_data))

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

for item in data:
    print(f"{item['title']}")

# print(data[0:2])
# for item in data:
#     print(item)