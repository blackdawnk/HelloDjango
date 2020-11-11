import requests

url = 'http://127.0.0.1:8000/rest/boards/4'

res = requests.get(url)

print(res)
print(res.text)