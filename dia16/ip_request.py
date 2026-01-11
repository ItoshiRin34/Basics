import requests

ip = requests.get("https://api.ipify.org").text
print("Seu IP público é:", ip)