# importa biblioteca
import os

# lista vazia
tarefas = []

# laço de repetição
while True:
    # usuário informa item da tarefa
    nova_tarefa = input('Insira a nova tarefa ou Enter para encerrar e exibir a lista: ')

    # verifica se o usuário inseriu nova tarefa
    if nova_tarefa != '':
        tarefas.append(nova_tarefa)
        continue
    else:
        break

# limpa console
os.system('cls')

# exibe a lista de taferas
print(f'{'-'*30} LISTA DE TAREFAS {'-'*30}\n')

for tarefa in tarefas:
    print(tarefa)