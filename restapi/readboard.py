import requests

url = 'http://127.0.0.1:8000/rest/boards'

res = requests.get(url)

print(res)
print(res.text)