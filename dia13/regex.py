import re

texto = """
Contato principal: joao.silva@gmail.com
Suporte: suporte@empresa.com.br
Inválido: teste@.com
Outro: admin123@yahoo.com
"""

padrao = r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z.]+"

emails = re.findall(padrao, texto)

for email in emails:
    print(email)
