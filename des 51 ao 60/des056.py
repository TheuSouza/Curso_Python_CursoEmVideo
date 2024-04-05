sdade = 0
masve = 0
masno = 0
d = 0
for c in range (0, 4):
    nome = str(input('Digite seu nome: '))
    dade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo F ou M: ')).strip().upper()
    sdade += dade
    if sexo == 'M' and masve < dade:
        masno = nome
        masve = dade
    elif sexo == 'F' and dade < 20:
        d += 1
print('A MÉDIA DE IDADE É: {}'.format(sdade / 4))
print('O HOMEM VAI VELHO É {} COM {} ANOS.'.format(masno, masve))
print('TOTAL DE MULHERES COM MENOS DE 20 ANOS É: {}'.format(d))




