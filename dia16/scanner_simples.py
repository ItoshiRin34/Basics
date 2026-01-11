import socket

PORTAS_COMUNS = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_portas(ip):
    print(f"\n🔍 Escaneando {ip}\n")

    for porta, servico in PORTAS_COMUNS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        resultado = sock.connect_ex((ip, porta))
        sock.close()

        if resultado == 0:
            print(f"🔥 Porta {porta} ABERTA → {servico}")
        else:
            print(f"❌ Porta {porta} fechada")

# TESTE — use seu próprio IP
scan_portas("")
