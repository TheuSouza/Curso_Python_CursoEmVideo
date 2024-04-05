banList = list()
banDict = dict()
muList = list()
totIdade = 0
while True:
    banDict['Nome'] = str(input('Nome: ')).strip().title()
    while True:
        banDict['Sexo'] = str(input('Sexo? [M/F]: ')).strip().upper()
        if banDict['Sexo'] in 'MF':
            break
        print('Erro!... Opção invalida, Digite [M] ou [F].')
    banDict['Idade'] = int(input('Idade: '))
    totIdade += banDict['Idade']
    if banDict['Sexo'] == 'F':
        muList.append(banDict['Nome'])
    banList.append(banDict.copy())
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if res == 'N':
        break
meed = totIdade / len(banList)
print('- ' * 25)
print(f'Foram Cadastrado um Total de {len(banList)} Pessoas.')
print(f'Média da Idade do Grupo é {meed:.1f} Anos.')
print(f'Mulheres Cadastradas: {muList}')
print('- ' * 25)
print('Pessoas com Idade Acima da Média:')
for d in banList:
    for k, c in d.items():
        if k == 'Idade' and c >= meed:
                print(f' - {d['Nome']} com {d['Idade']} Anos.')
print('- ' * 25)







