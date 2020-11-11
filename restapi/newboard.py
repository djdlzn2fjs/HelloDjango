import requests
#from datetime import datetime


url = 'http://127.0.0.1:8000/rest/boards/create/'

#today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

data = {'title': '이글이 보이나요?', 'contents': '새글새글',
        'userid': '새글새글'}

res = requests.put(url, data=data)

print(res)
print(res.text)
