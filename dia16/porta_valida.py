def validar_porta(texto):
    if not texto.isdigit():
        return False

    porta = int(texto)
    return 0 <= porta <= 65535


# teste
while True:
    p = input("Digite uma porta (ou sair): ")

    if p.lower() == "sair":
        break

    if validar_porta(p):
        print("✅ Porta válida")
    else:
        print("❌ Porta inválida")
