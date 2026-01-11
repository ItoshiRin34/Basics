import ipaddress

def validar_ip(texto: str) -> bool:
    try:
        ipaddress.ip_address(texto.strip())
        return True
    except ValueError:
        return False

# teste rápido
if __name__ == "__main__":
    while True:
        ip = input("Digite um IP (ou 'sair'): ").strip()
        if ip.lower() == "sair":
            break

        if validar_ip(ip):
            print("✅ IP válido")
        else:
            print("❌ IP inválido")
