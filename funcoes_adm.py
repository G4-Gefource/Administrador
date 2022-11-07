import os
import msvcrt

# FUNÇÕES


def limpar():  # FUNÇÃO PARA LIMPAR A TELA
    os.system("cls")


def pausa():  # FUNÇÃO PARA PAUSAR O SISTEMA
    print('\nPressione qualquer tecla para continuar...\n')
    char = msvcrt.getch()

def menu():  # FUNÇÃO PARA MENU 
    print('1 - Adicionar\n')
    print('2 - Remover \n')
    print('3 - Visualizar os serviços\n')
    print('0 - Sair\n')
    
#Função Olá mundo
def apresentacao():
    print("Olá seja bem vindo ao setor administrativo do Eventum\n")
    print("Por favor adicione as informações do seu serviço a seguir\n")

#Função adicionar
def adicionar(servico):
    servico.append(input("Adicione as informações sobre o nome do serviço: "))

    servico.append(input("Adicione as informações sobre o local do serviço: "))

    servico.append(input("Adicione as informações o que ira prestar no serviço: "))

    return servico

#Função remover
def remover(servico):
    auxremover=input(f"Deseja remover {servico}?")
    if auxremover[0] == 'S' or auxremover[0] == 's':
        servico.clear()
        print("O serviço 1 foi removido")
    else:
        print("O serviço não foi removido")
    return servico
    


