galera = list()
dado = list()
totReg = 0
lisMenor = list()
lisMaior = list()

while True:
    dado.append(str(input('Nome: ')).strip())
    dado.append(float(input('Peso Kg: ')))
    galera.append(dado[:])
    totReg += 1
    dado.clear()
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continur [S/N]: ')).strip().upper()
    if res == 'N':
        break

for li in galera:
    if li[1] <= 70:
        lisMenor.append(li[0])
    elif li[1] >= 100:
        lisMaior.append(li[0])

print(f'Total de Pessoas cadastradas: {totReg}')
print(f'Total de Pessoas abaixo de 70Kg: {lisMenor}')
print(f'Total de Pessoas Acima de 100KG: {lisMaior}')

