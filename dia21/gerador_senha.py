import secrets
import string

def gerar_senha(tamanho=16, usar_simbolos=True):
    if tamanho < 12:
        raise ValueError("Use no mínimo 12 caracteres (ideal 16+).")

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = "!@#$%^&*()-_=+[]{};:,.?/"

    pool = letras_maiusculas + letras_minusculas + numeros
    if usar_simbolos:
        pool += simbolos

    # Garante pelo menos 1 de cada categoria (pra não sair “forte por sorte”)
    senha = [
        secrets.choice(letras_maiusculas),
        secrets.choice(letras_minusculas),
        secrets.choice(numeros),
    ]
    if usar_simbolos:
        senha.append(secrets.choice(simbolos))

    # Completa o resto
    while len(senha) < tamanho:
        senha.append(secrets.choice(pool))

    # Embaralha pra não ficar previsível (ex: sempre começa com maiúscula)
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)

if __name__ == "__main__":
    qtd = int(input("Tamanho (recomendado 16 ou 20): ").strip() or "16")
    simbolos = input("Usar símbolos? (s/n): ").strip().lower() != "n"
    print("Senha gerada:", gerar_senha(qtd, simbolos))
