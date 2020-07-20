import requests

BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'video/1', {'name': "Youtube", 'views': 100, 'likes': 10})

print(response.json())

input()

response = requests.get(BASE + 'video/8')

print(response.json())
