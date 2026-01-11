import requests

url = "https://site.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

resposta = requests.get(url, headers=headers)

print(resposta.status_code)
print(resposta.text[:500])
