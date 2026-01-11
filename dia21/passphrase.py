import secrets

PALAVRAS = [
    "cafe", "lua", "tigre", "azul", "vento", "pedra", "fogo", "neve",
    "mar", "sol", "nuvem", "eco", "raio", "folha", "ponte", "chave",
    "lobo", "tempo", "sombra", "porto", "rio", "noite", "brisa"
]

def gerar_passphrase(qtd_palavras=4, separador="-", adicionar_numeros=True):
    if qtd_palavras < 4:
        raise ValueError("Use no mínimo 4 palavras.")

    palavras = [secrets.choice(PALAVRAS) for _ in range(qtd_palavras)]
    frase = separador.join(palavras)

    if adicionar_numeros:
        frase += separador + str(secrets.randbelow(90) + 10)

    return frase

if __name__ == "__main__":
    print("Passphrase gerada:")
    print(gerar_passphrase())
