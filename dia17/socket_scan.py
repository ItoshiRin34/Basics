import socket

ip = "1"   # localhost (sua própria máquina)
porta = 3306         # exemplo

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)  # evita travar

resultado = sock.connect_ex((ip, porta))

if resultado == 0:
    print(f"✅ Porta {porta} ABERTA")
else:
    print(f"❌ Porta {porta} FECHADA")

sock.close()
