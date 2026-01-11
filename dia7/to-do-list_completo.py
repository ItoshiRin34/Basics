def Adicionar(lista_tarefas):
    tarefa = input("Anote uma tarefa:\n")
    lista_tarefas.append(tarefa)

def Exibir(lista_tarefas):
    print("\nSuas Tarefas:")
    for numero, t in enumerate(lista_tarefas, start=1):
        print(numero,"-", t,"\n")
   
def Remover(lista_tarefas):
    try:
        deletar = int(input("Digite o numero da tarefa para ser excluida: "))

    except ValueError:
        print("Isso nao e um numero")
        return
    
    if deletar < 1 or deletar > len(lista_tarefas):
        print("Nao foi possivel")
        return
    lista_tarefas.pop(deletar - 1)


lista_tarefas = []

while True:
    print("--------MENU--------\n1- Adicionar Tarefa\n2- Exibir Tarefas\n3- Excluir Tarefa\n4- Sair\n")
    select = input("Selecione: ")

    if select == "1":
        Adicionar(lista_tarefas)


    if select == "2":
        Exibir(lista_tarefas)
  

    if select == "3":
        Remover(lista_tarefas)
   

    if select =="4":
        break
