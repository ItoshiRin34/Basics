lista_nomes = []

while True:
    nome = input("Digite um nome ou 'sair': ")
    if nome.lower() == "sair":
        break

    lista_nomes.append(nome)

print("\nLista de nomes: ")

for n in lista_nomes:
    print("-", n)