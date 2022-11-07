import funcoes_adm

funcoes_adm.limpar()
funcoes_adm.apresentacao()

servico=[]
servico1=[]
servico2=[]
servico3=[]

#Ajuste de variavel 
cont=0

servico.append(input("Adicione as informações sobre o nome do serviço: "))

servico.append(input("Adicione as informações sobre o local do serviço: "))

servico.append(input("Adicione as informações o que ira prestar no serviço: "))
cont+=1

aux=1
funcoes_adm.limpar()



while aux==1:
    funcoes_adm.limpar()
    funcoes_adm.menu()
    escolha=int(input(" "))

    #Variavel do fluxo do programa
    flux=1

    
    while flux == 1:
        if escolha==1:

            if cont==0:
                
                funcoes_adm.limpar()
                print(f"Você esta adicionando o serviço no slot {cont+1}")
                funcoes_adm.adicionar(servico)

                print("\nServiço adicionado com sucesso!")
                funcoes_adm.pausa()
                cont+=1
                
                flux=0
           
            elif cont==1:
                
                funcoes_adm.limpar()
                print(f"Você esta adicionando o serviço no slot {cont+1}")
                funcoes_adm.adicionar(servico1)

                print("\nServiço adicionado com sucesso!")
                funcoes_adm.pausa()
                cont+=1
                
                flux=0

            elif cont==2:
                funcoes_adm.limpar()
                print(f"Você esta adicionando o serviço no slot {cont+1}")
                funcoes_adm.adicionar(servico2)

                print("\nServiço adicionado com sucesso!")
                funcoes_adm.pausa()
                cont+=1
                flux=0

            elif cont==3:
                funcoes_adm.limpar()
                print(f"Você esta adicionando o serviço no slot {cont+1}")
                funcoes_adm.adicionar(servico3)

                print("\nServiço adicionado com sucesso!")
                funcoes_adm.pausa()
                
                flux=0
            else:
                print("Esta opção não existe")
                flux=0

 
        elif escolha ==2:
            print("Você esta na opção de remover o serviço\n")

            print("Digite um numero de 1 a 4 para que o serviço seja removido")

            remover=int(input())
            if remover == 1:
                funcoes_adm.remover(servico)
                funcoes_adm.pausa()
                flux=0
                cont=0

            elif remover == 2:
                funcoes_adm.remover(servico1)
                funcoes_adm.pausa()
                flux=0
                cont=1

            elif remover == 3:
                funcoes_adm.remover(servico2)
                funcoes_adm.pausa()
                flux=0
                cont=2

            elif remover == 4:
                funcoes_adm.remover(servico3)
                funcoes_adm.pausa()
                flux=0
                cont=3

            else:
                print("Este serviço não existe")
                funcoes_adm.pausa()
                flux=0


        elif escolha==3:
            print("Escolha o serviço a ser visualizado:")
            op=int(input())

            if op ==1:
                funcoes_adm.limpar()
                print(servico)
                funcoes_adm.pausa()
                flux=0

            elif op==2:
                funcoes_adm.limpar()
                print(servico1)
                funcoes_adm.pausa()
                flux=0

            elif op==3:
                funcoes_adm.limpar()
                print(servico2)
                funcoes_adm.pausa()
                flux=0

            elif op==4:
                funcoes_adm.limpar()
                print(servico3)
                funcoes_adm.pausa()
                flux=0

            else:
                funcoes_adm.limpar()
                print("Este serviço não existe")
                funcoes_adm.pausa()
                flux=0

        elif escolha==0:
            funcoes_adm.limpar()
            print("Obrigado por utilazar o modo administrativo do EVENTUM")
            flux=0
        
        else:
            funcoes_adm.limpar()
            print("Opção não existe")
            funcoes_adm.pausa()
            flux=0

