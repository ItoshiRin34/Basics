def Adicionar():
    pass
def Exibir():
    pass
def Remover():
    pass
def Sair():
    pass

lista_tarefas = []

while True:
    print("--------MENU--------\n1- Adicionar Tarefa\n2- Exibir Tarefas\n3- Excluir Tarefa\n4- Sair\n")
    select = input("Selecione: ")

    if select == "1":
        tarefa = input("Anote uma tarefa:\n")
        lista_tarefas.append(tarefa)

    if select == "2":
        print("\nSuas Tarefas:")
        for numero, t in enumerate(lista_tarefas, start=1):
            print(numero,"-", t,"\n")

    if select == "3":
        deletar = input("Digite o numero da tarefa para ser excluida: ")
        deletar = int(deletar)
        lista_tarefas.pop(deletar - 1)

    if select =="4":
        break
