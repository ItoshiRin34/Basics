import os
import random

pasta = "/home/"
arquivos = os.listdir(pasta)

for arquivo in arquivos:
    numero = random.randint(100,999)
    nome_antigo = os.path.join(pasta, arquivo)
    novo_nome = os.path.join(pasta, f"arquivo_{numero}.txt")

    os.rename(nome_antigo, novo_nome)
