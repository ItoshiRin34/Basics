import requests
from bs4 import BeautifulSoup

url = "https://pt.wikipedia.org/wiki/Pato"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

resposta = requests.get(url, headers=headers)

print(resposta.status_code)

soup = BeautifulSoup(resposta.text, "html.parser")

titulos = soup.find_all(["h1", "h2"])

for titulo in titulos:
    print(titulo.text.strip())
