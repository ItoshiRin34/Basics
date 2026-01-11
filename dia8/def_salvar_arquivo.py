def dados():
    nome = input("Qual seu nome? ")
    idade = input("Quantos anos tem? ")
    altura = input("Quanto de altura? ")
    peso = input("Quanto voce pesa? ")
    carro = input("Tem carro? ")

    return nome, idade, altura, peso, carro


def salvar(nome, idade, altura, peso, carro):
    with open("Dados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Altura: {altura}\n")
        arquivo.write(f"Peso: {peso}\n")
        arquivo.write(f"Carro: {carro}\n")
        arquivo.write("\n")

    print("Dados salvos.")


def ler():
    with open("Dados.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    return conteudo


# ===== PROGRAMA PRINCIPAL =====

nome, idade, altura, peso, carro = dados()
salvar(nome, idade, altura, peso, carro)

conteudo = ler()
print(conteudo)
