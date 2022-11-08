import funcoes_adm

funcoes_adm.limpa()

# PONTOS TURÍSTICOS CADASTRADOS
pontos = [{'NOME': 'RESTAURANTE A', 'NOTA': 9.45,
           'LOCALIZAÇÃO': '300m de distância'},
          {'NOME': 'BAR B', 'NOTA': 9.05,
           'LOCALIZAÇÃO': '600m de distância'},
          {'NOME': 'PRAIA C', 'NOTA': 8.75,
           'LOCALIZAÇÃO': '100m de distância'},
          {'NOME': 'PASSEIO D', 'NOTA': 8.50,
           'LOCALIZAÇÃO': '1km de distância'},
          {'NOME': 'CAFÉ E', 'NOTA': 9.85,
           'LOCALIZAÇÃO': '400m de distância'},
          {'NOME': 'LUAU F', 'NOTA': 7.95,
           'LOCALIZAÇÃO': '800m de distância'}]

op = 1
print('BEM VINDO AO SETOR ADMINISTRATIVO DO EVENTUM!\n')
while op != 0:
    funcoes_adm.menu()
    op = int(input('Selecione uma das opções e tecle ENTER: '))
    funcoes_adm.limpa()
    if op == 1:
        d = {'NOME': '', 'NOTA': 0.0, 'LOCALIZAÇÃO': ''}
        d['NOME'] = input('Informe o nome do estabelecimento: ').upper()
        d['NOTA'] = float(input('Informe a nota do estabelecimento: '))
        d['LOCALIZAÇÃO'] = input('Informe a distância do ponto para o hotel: ')
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
            print('Esse ponto tá aqui ó')
        funcoes_adm.pausa()
    elif op == 3:
        for i in range(len(pontos)):
            funcoes_adm.exibe_ponto(pontos[i])
            funcoes_adm.pausa()
    elif op == 4:
        nome = input(
            'Informe o nome do estabelecimento que deseja atualizar: ').upper()
        ponto_local = list(filter(lambda p: p['NOME'] == nome, pontos))
        if len(ponto_local) < 1:
            print('Este ponto não está registrado.')
        else:
            print('Esse ponto tá aqui ó')
        funcoes_adm.pausa()
    elif op == 5:
        print()
    funcoes_adm.limpa()
