liss = []
par = []
impar = []
while True:
    liss.append(int(input('Digite um valor: ')))
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if res in 'N':
        break
print('- ' * 20)
print(f'Lista completa: {liss}')
print('- ' * 20)
for c in liss:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Lista de par: {par}')
print(f'Lista de impar: {impar}')

