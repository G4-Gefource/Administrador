import funcoes_adm

funcoes_adm.limpar()
funcoes_adm.apresentacao()

servico=[] 
servico1=[] 
servico2=[]
servico3=[]

servico.append(input("Adicione as informações sobre o nome do serviço: "))

servico.append(input("Adicione as informações sobre o local do serviço: "))

servico.append(input("Adicione as informações o que ira prestar no serviço: "))

aux=1
funcoes_adm.limpar()

while aux==1:
    funcoes_adm.limpar()
    funcoes_adm.menu()
    escolha=int(input(" "))
    flux=1
    servcont=1

    while flux == 1:
        if escolha==1:


            if servcont==1:
                funcoes_adm.limpar()
                servico1.append(input("Adicione as informações sobre o nome do serviço: "))

                servico1.append(input("Adicione as informações sobre o local do serviço: "))

                servico1.append(input("Adicione as informações o que ira prestar no serviço: "))

                servcont+=1
                flux=0

            elif servcont==2:
                funcoes_adm.limpar()
                servico2.append(input("Adicione as informações sobre o nome do serviço: "))

                servico2.append(input("Adicione as informações sobre o local do serviço: "))

                servico2.append(input("Adicione as informações o que ira prestar no serviço: "))

                servcont+=1
                flux=0

            elif servcont==3:
                funcoes_adm.limpar()
                servico3.append(input("Adicione as informações sobre o nome do serviço: "))

                servico3.append(input("Adicione as informações sobre o local do serviço: "))

                servico3.append(input("Adicione as informações o que ira prestar no serviço: "))
                flux=0

            else:
                print("Esta opção não existe")
                flux=0


 
        elif escolha ==2:
            print("Você esta na opção de remover o serviço\n")

            print("Digite um numero de 1 a 4 para que o serviço seja removido")

            remover=int(input())
            if remover == 1:
                auxremover=input(f"Deseja remover {servico}?")

                if auxremover[0] == 'S' or auxremover[0] == 's':
                    servico.clear
                    print("O serviço 1 foi removido")

                else:
                    print("O serviço não foi removido")
                    flux=0

            if remover == 2:
                auxremover=input(f"Deseja remover {servico1}?")

                if auxremover[0] == 'S' or auxremover[0] == 's':
                    servico1.clear
                    print("O serviço 1 foi removido")

                else:
                    print("O serviço não foi removido")
                    flux=0

            if remover == 3:
                auxremover=input(f"Deseja remover {servico2}?")

                if auxremover[0] == 'S' or auxremover[0] == 's':
                    servico2.clear
                    print("O serviço 1 foi removido")

                else:
                    print("O serviço não foi removido")
                    flux=0

            if remover == 4:
                auxremover=input(f"Deseja remover {servico3}?")

                if auxremover[0] == 'S' or auxremover[0] == 's':
                    servico3.clear
                    print("O serviço 1 foi removido")

                else:
                    print("O serviço não foi removido")
                    flux=0


        elif escolha==3:
            print("Escolha o serviço a ser visualizado:")
            op=int(input())
            if op ==1:
                funcoes_adm.limpar()
                print(servico)
                flux=0
            elif op==2:
                funcoes_adm.limpar()
                print(servico1)
                flux=0
            elif op==3:
                funcoes_adm.limpar()
                print(servico2)
                flux=0
            elif op==4:
                funcoes_adm.limpar()
                print(servico3)
                flux=0
            else:
                funcoes_adm.limpar()
                print("Este serviço não existe")
                flux=0

        elif escolha==4:
            funcoes_adm.limpar()
            print("Obrigado por utilazar o modo administrativo do EVENTUM")
            flux=0
        
        else:
            funcoes_adm.limpar()
            print("Opção nao existe")
            flux=0


