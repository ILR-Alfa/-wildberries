import requests

url = "https://static-basket-01.wbbasket.ru/vol0/data/main-menu-ru-ru-v3.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
print(response.status_code)  
print(response.text[:500])   