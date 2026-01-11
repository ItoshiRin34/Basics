import itertools

palavra_base = input("Palavra base: ")

numeros = ["", "123", "2024", "77"]
simbolos = ["", "@", "#", "!", "*"]

with open("wordlist.txt", "w") as f:
    for n, s in itertools.product(numeros, simbolos):
        f.write(f"{palavra_base}{s}{n}\n")
        f.write(f"{palavra_base.capitalize()}{s}{n}\n")

print("Wordlist gerada com sucesso!")
