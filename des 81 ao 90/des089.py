boletim = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1] + dados[2]) / 2)
    boletim.append(dados[:])
    dados.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]: ')).strip().upper()
    if res == 'N':
        break
print('-' * 20)
print(f'{"Nº":^3} {"Nome":^10} {"Média":^5}')
print('-' * 20)
for pos, bo in enumerate(boletim):
    print(f'{pos:<3} {bo[0]:<10} {bo[3]:^5}')
print('-' * 20)
while True:
    res = int(input('Mostrar as Notas de qual Aluno? (999) Para Parar.'))
    if res == 999:
        break
    print(f'Todas as nota do aluno {boletim[res][0].upper()} foram {boletim[res][1]} e {boletim[res][2]}.')
print('Acabou...')



