import sys

if len(sys.argv) < 2:
    print("Uso: python saudacao.py <seu_nome>")
else:
    nome = sys.argv
    print(f"Olá, {nome}!")
