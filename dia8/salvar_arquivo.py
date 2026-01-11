nome = input("Qual seu nome?")
idade = input("Quantos anos tem?")
altura = input("Quanto de altura?")
peso = input("Quanto voce pesa?")
carro = input("Tem carro?")

with open("Dados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}\n")
    arquivo.write(f"Altura: {altura}\n")
    arquivo.write(f"Peso: {peso}\n") 
    arquivo.write(f"carro: {carro}\n")
    arquivo.write(f"\n")

print("Dados salvos.")

with open("Dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
print(conteudo)
