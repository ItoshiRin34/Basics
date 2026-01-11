import requests
import re

url = "https://unisanta.br/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers=headers)

html = resposta.text

padrao = r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z.]+"

emails = re.findall(padrao, html)

emails_unicos = set(emails)

for email in emails_unicos:
    print(email)
