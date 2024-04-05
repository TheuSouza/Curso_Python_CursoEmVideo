from time import sleep
jogador = dict()
golsfeito = list()
totgols = 0
jogador['Nome'] = str(input('Nome do Jogador: ')).strip().title()
nu = int(input(f'Quantas partidas {jogador['Nome']} Jogou? '))
for c in range(nu):
    gols = int(input(f'Gols na {c + 1}º Partida? '))
    golsfeito.append(gols)
    totgols += gols
jogador['Gols'] = golsfeito.copy()
print('- ' * 25)
print('{:^50}'.format(' APROVEITAMENTO '))
print('- ' * 25)
print(f'Gols feito em cada Partida: {jogador['Gols']} \nTotal de {totgols} Gols.')
print('- ' * 25)
print(f'O Jogador {jogador['Nome']} Jogou um Total de {nu} Partidas.')
for cont, c in enumerate(golsfeito):
    print(f'  -> Na {cont + 1}º Partida, Fez {c} Gols.')

