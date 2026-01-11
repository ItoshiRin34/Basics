
def cadastro():
    while True:
        try:
            idade = int(input("Sua idade: "))
            return idade
            

        except ValueError:
            print("Invalida")

idade_usuario = cadastro()
print(f"Idade cadastrada! {idade_usuario}")