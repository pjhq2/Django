import requests

for i in range(1, 60):
    url = f'http://127.0.0.1:8000/articles/{i}/delete/'
    requests.get(url)