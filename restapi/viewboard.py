import requests

url = 'http://127.0.0.1:8000/rest/boards/1'

res = requests.get(url)
res = requests.delete(url)

print(res)
print(res.text)