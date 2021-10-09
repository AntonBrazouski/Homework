import requests 

response = requests.get('https://news.yahoo.com/rss/')

print(response.status_code)

# response.json
print(response.text[0:200])
print(response.text[-200:])
print(type(response.text))
print(len(response.text))