import socket

ip = "1"
porta = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

if sock.connect_ex((ip, porta)) == 0:
    sock.send(b"GET / HTTP/1.1\r\nHost: teste\r\n\r\n")
    resposta = sock.recv(1024)

    if resposta.startswith(b"HTTP/"):
        print("✅ Porta aberta e serviço HTTP confirmado")
    else:
        print("⚠️ Porta aberta, mas não é HTTP")
else:
    print("❌ Porta fechada")

sock.close()
