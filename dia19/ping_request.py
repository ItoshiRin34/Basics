import os
import time

alvo = "8.8.8.8"

while True:
    resposta = os.system(f"ping -c 1 {alvo} > /dev/null")

    if resposta == 0:
        print("Host ATIVO")
    else:
        print("Host OFFLINE")

    time.sleep(2)
