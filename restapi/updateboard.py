import requests
from datetime import datetime


url = 'http://127.0.0.1:8000/rest/boards/2/'

today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

data = {'title': '수정됨2', 'contents': '수정됨2',
        'userid': '수정됨2', 'regdate': today}

res = requests.put(url, data=data)

print(res)
print(res.text)
