print('=-' * 20)
print(f'{"  CONTANDO NÚMEROS 2.0  ":=^40}')
print('=-' * 20)
nu = 0
res = ''
c = 0
s = 0
mnor = 0
mior = 0
while res != 'N':
    nu = int(input('Digite Números: '))
    if c == 0:
        mnor = nu
        mior = nu
    else:
        if mnor > nu:
            mnor = nu
        elif mior < nu:
            mior = nu
    c += 1
    s += nu
    res = str(input('Quer continuar [S/N]: ')).strip().upper()
med = s / c
print('A média foi {:.2f}.'.format(med))
print('Maior valor foi {}.'.format(mior))
print('Menor valor foi {}.'.format(mnor))




