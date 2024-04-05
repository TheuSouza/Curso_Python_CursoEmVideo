from time import sleep
dados = dict()
jogadores = list()
golsFeito = list()
while True:
    print('- ' * 25)
    totgols = 0
    golsFeito.clear()
    dados['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    dados['Partida'] = int(input(f'Quantas partidas Jogou? '))
    for c in range(dados['Partida']):
        gols = int(input(f'Gols na {c + 1}º Partida? '))
        golsFeito.append(gols)
        totgols += gols
    dados['Total de Gols'] = totgols
    dados['Gol Por Partida'] = golsFeito[:]
    jogadores.append(dados.copy())
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if res == 'N':
        break
print('- ' * 30)
print('{:^50}'.format(' APROVEITAMENTO '))
print('- ' * 30)
print(f'{" Cod ":=^5} {" Nome ":=^10} {" Total ":=^8} {" Gols Por Partida ":=^20}')
for cont, jo in enumerate(jogadores):
    print(f'{cont:^5} {jo['Nome']:<10} {jo['Total de Gols']:^8}    {jo['Gol Por Partida']} ')
print('- ' * 30)
print('{:^50}'.format(' LEVANTAR DADOS JOGADOR '))
print('- ' * 30)
while True:
    golsFeito.clear()
    mos = int(input('Quer Levantar Dados de Qual Jogador: '))
    if mos == 999:
        break
    if mos >= len(jogadores):
        print('\033[1;31mOpção Invalida...\033[m Não Existe Jogador Com esse Codigo.')
    else:
        golsFeito.append(jogadores[mos])
        for i in golsFeito:
            print(f'\033[1;34mO Jogador {i['Nome']}\033[m')
            for pos, c in enumerate(i['Gol Por Partida']):
                print(f'No {pos + 1}º Jogo Fez {c} Gols.')






