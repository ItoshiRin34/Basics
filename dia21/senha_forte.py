import re

def validar_senha(senha):
    if len(senha) < 8:
        return "❌ Muito curta (mínimo 8 caracteres)"

    if not re.search(r"[A-Z]", senha):
        return "❌ Falta letra MAIÚSCULA"

    if not re.search(r"[a-z]", senha):
        return "❌ Falta letra minúscula"

    if not re.search(r"[0-9]", senha):
        return "❌ Falta número"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return "❌ Falta caractere especial"

    return "✅ Senha forte"

senha = input("Digite sua senha: ")
print(validar_senha(senha))
