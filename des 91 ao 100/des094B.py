galera = list()
dados = dict()
soma = media = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro!... Digite uma opção valida [M] ou [F].')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    galera.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro!... Digite uma opção valida [S] ou [N].')
    if resp in 'N':
        break
media = soma / len(galera)
print(' - ' * 25)
print(f'Ao todo tempos {len(galera)} Pessoas cadastradas.')
print(f'A media de idade foi {media:.2f} Anos.')
print('Total de mulheres cadastradas foram: ', end='')
for e in galera:
    if e['sexo'] in 'F':
        print(f'{e["nome"]}', end=' ')
print()
print('Total de Pessoas acima da média: ')
for e in galera:
    if e['idade'] >= media:
        print('    ')
        for v in e.items():
            print(f'{v[0]} = {v[1]} ', end='')
        print()
print('Finalizado...')
