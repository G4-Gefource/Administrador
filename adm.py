import funcoes_adm

funcoes_adm.limpa()

# PONTOS TURÍSTICOS CADASTRADOS
pontos = [{'NOME': 'RESTAURANTE A', 'NOTA': 9.45,
           'LOCALIZAÇÃO': '300m de distância',
           'DESCRIÇÃO':
           'Restaurante familiar, bem localizado, com uma grande variedade de comidas regionais.'},
          {'NOME': 'BAR B', 'NOTA': 9.05,
           'LOCALIZAÇÃO': '600m de distância',
           'DESCRIÇÃO':
           'Bar conhecido por noites com música e preço baixo.'},
          {'NOME': 'PRAIA C', 'NOTA': 8.75,
           'LOCALIZAÇÃO': '100m de distância',
           'DESCRIÇÃO':
           'Uma das praias mais procuradas de Maceió, o local perfeito para aproveitar um dia de sol.'},
          {'NOME': 'PASSEIO D', 'NOTA': 8.50,
           'LOCALIZAÇÃO': '1km de distância',
           'DESCRIÇÃO':
           'Um passeio inesquecível para Maceió, preço baixo e melhor qualidade.'},
          {'NOME': 'CAFÉ E', 'NOTA': 9.85,
           'LOCALIZAÇÃO': '400m de distância',
           'DESCRIÇÃO':
           'Ambiente familiar, com uma grande variedade de refeições para agradar todos os gostos.'},
          {'NOME': 'LUAU F', 'NOTA': 7.95,
           'LOCALIZAÇÃO': '800m de distância',
           'DESCRIÇÃO':
           'Um ambiente ideal para casais que querem aproveitar o Maceió da forma mais romântica.'}]

op = 1
print('BEM VINDO AO SETOR ADMINISTRATIVO DO EVENTUM!\n')
while op != 0:
    funcoes_adm.menu()
    op = int(input('Selecione uma das opções e tecle ENTER: '))
    funcoes_adm.limpa()
    if op == 1:
        d = {'NOME': '', 'NOTA': 0.0, 'LOCALIZAÇÃO': '', 'DESCRIÇÃO': ''}
        d['NOME'] = input('Informe o nome do estabelecimento: ').upper()
        d['NOTA'] = float(input('Informe a nota do estabelecimento: '))
        d['LOCALIZAÇÃO'] = input('Informe a distância do ponto para o hotel: ')
        d['DESCRIÇÃO'] = input('Informe a descrição do ponto: ')
        pontos.append(d)
        print('Ponto adicionado com sucesso!')
        funcoes_adm.pausa()
    elif op == 2:
        nome = input(
            'Informe o nome do estabelecimento que deseja atualizar: ').upper()
        ponto_local = list(filter(lambda p: p['NOME'] == nome, pontos))
        if len(ponto_local) < 1:
            print('Este ponto não está registrado.')
        else:
            print(f'Informe as atualizações do ponto {(ponto_local[0]["NOME"]).title()}')
            d = {'NOTA': 0.0, 'LOCALIZAÇÃO': '', 'DESCRIÇÃO': ''}
            print(f'Nota anterior: {ponto_local[0]["NOTA"]}')
            d['NOTA'] = float(input('Informe a nova nota: '))
            print(f'Localização anterior: {ponto_local[0]["LOCALIZAÇÃO"]}')
            d['LOCALIZAÇÃO'] = input('Informe a nova localização: ')
            print(f'Descrição anterior: {ponto_local[0]["DESCRIÇÃO"]}')
            d['DESCRIÇÃO'] = input('Informe a nova descrição: ')
            ponto_local[0].update(d)
            print('Ponto atualizado com sucesso!')
        funcoes_adm.pausa()
    elif op == 3:
        for i in range(len(pontos)):
            funcoes_adm.exibe_ponto(pontos[i])
            funcoes_adm.pausa()
    elif op == 4:
        nome = input(
            'Informe o nome do estabelecimento que deseja remover: ').upper()
        ponto_local = list(filter(lambda p: p['NOME'] == nome, pontos))
        if len(ponto_local) < 1:
            print('Este ponto não está registrado.')
        else:
            print(f'Tem certeza que deseja deletar o ponto {ponto_local[0]["NOME"]}?')
            cert = input('').upper()
            if cert[0] == 'S':
                pontos.remove(ponto_local[0])
                print('Ponto removido com sucesso!')
            else:
                print('Operação cancelada com successo!.')
        funcoes_adm.pausa()
    elif op == 5:
        print()
    elif op == 0:
        print('Operação encerrada.')
        funcoes_adm.pausa()
    else:
        print('Opção inválida.')
        funcoes_adm.pausa()
    funcoes_adm.limpa()
