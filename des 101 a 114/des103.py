def ficha(no='', go=''):
    if no == '':
        no = 'Desconhecido'
    if go == '':
        go = 0
    print(f'O jogador {no} fez {go} Gols no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Gols feito: '))
ficha(nome, gols)
