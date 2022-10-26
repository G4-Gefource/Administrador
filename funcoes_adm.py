import os
import msvcrt

# FUNÇÕES

def limpar():  
    os.system("cls")

def pausa(): 
    print('\nPressione qualquer tecla para continuar...\n')
    char = msvcrt.getch()

def menu():
    print('1 - Adicionar\n')
    print('2 - Remover \n')
    print('3 - Visualizar os serviços\n')
    print('0 - Sair\n')

def apresentacao():
    print("Olá seja bem vindo ao setor administrativo do Eventum\n")
    print("Por favor precione 1 para adicionar as informaçoes do seu serviços: \n")
