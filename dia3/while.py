username = "Coxinha"
senha = "123321"

tentativas = 3

while tentativas > 0:
    username = input("Username: ")
    senha = input("Senha: ")
    if username == "Coxinha" and senha == "123321":
        print("Logado!")
        break
    else:
        print("Username ou senha errado!")
        tentativas -=1

if tentativas == 0:
    print("Conta bloqueada!")