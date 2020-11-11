import requests

url = 'http://127.0.0.1:8000/rest/boards/create'

data = {'userid': '수정됨2','title': '수정됨2', 'contents': '수정됨2'}
res = requests.post(url, data=data)

print(res)
print(res.text)
