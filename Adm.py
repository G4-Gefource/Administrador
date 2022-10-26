import funcoes_adm


print(funcoes_adm.apresentacao())
print()
escolha=int(input(''))

dicio={}

if escolha==1:
    add=[]
    add.append(input("Digite o nome do seu primeiro serviço: "))
    add.append(input(f"Digite o local do serviço {add[0]}: "))
    add.append(input("Digite um serviço que ira prestar: "))
    dicio[0]=add
    print(dicio)
    #print(funcoes_adm.limpar())

escolha=0 

print(funcoes_adm.menu)
print()
escolha=int(input(''))

if escolha==1:
    add_2=[]
    add_2.append(input("Digite nome do serviço: "))
    add_2.append(input(f"Digite o local do serviço {add_2[0]}: "))
    add_2.append(input("Digite um serviço que ira prestar: "))
    print()







