import re

texto = """
Contato: joao@gmail.com
Suporte: suporte@empresa.com
Email errado: teste@.com
"""

padrao = r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]+"

# 1️⃣ FINDALL — extrair
emails = re.findall(padrao, texto)
print("Emails encontrados:")
print(emails)

# 2️⃣ FULLMATCH — validar
email_usuario = "admin@gmail.com"

if re.fullmatch(padrao, email_usuario):
    print("Email válido")
else:
    print("Email inválido")

# 3️⃣ SUB — substituir / limpar
texto_limpo = re.sub(padrao, "[EMAIL]", texto)
print("\nTexto limpo:")
print(texto_limpo)
