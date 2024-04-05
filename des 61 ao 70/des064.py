print('=-' * 20)
print(f'{"  CONTANDO NÚMEROS  ":=^40}')
print('=-' * 20)
nu = 0
c = 0
s = 0
while nu != 999:
    nu = int(input('Digite Números: '))
    c += 1
    s += nu
print('Você digitou um total de {} Números.'.format(c - 1))
print('A soma de todos os númeors foi {}.'.format(s - 999))


'''nu = int(input('Digite Números: '))
while nu != 999:
    c += 1
    s += nu
    nu = int(input('Digite Números: '))
print('Você digitou um total de {} Números.'.format(c))
print('A soma de todos os númeors foi {}.'.format(s))'''