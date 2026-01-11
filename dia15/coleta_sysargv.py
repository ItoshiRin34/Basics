import requests
import re
import sys

# argv[0] = nome do script
# argv[1] = primeiro argumento (URL)

if len(sys.argv) < 2:
    print("Uso: python coleta_email.py <url>")
    sys.exit()

url = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers=headers)
html = resposta.text

padrao = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,24}"

emails = re.findall(padrao, html)
emails_unicos = set(emails)

for email in emails_unicos:
    print(email)
