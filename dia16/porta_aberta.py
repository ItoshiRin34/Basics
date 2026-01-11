import socket

def porta_aberta(ip, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    resultado = sock.connect_ex((ip, porta))
    sock.close()

    return resultado == 0


# teste
ip =
porta = 20

if porta_aberta(ip, porta):
    print(f"🔥 Porta {porta} ABERTA")
else:
    print(f"❌ Porta {porta} FECHADA")
