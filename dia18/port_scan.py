import socket

alvo = "youtube.com"  # IP que você quer escanear
portas = [21, 22, 80, 443]

print(f"Escaneando o alvo: {alvo}\n")

for porta in portas:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    resultado = sock.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"[+] Porta {porta} ABERTA")
    else:
        print(f"[-] Porta {porta} fechada")

    sock.close()
