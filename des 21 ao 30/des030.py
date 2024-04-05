nu = int(input('Digite um número: '))
if nu % 2 == 0:
    print('{} é PAR!'.format(nu))
else:
    print('{} é IMPAR!'.format(nu))

print('É Par 'if nu % 2 == 0 else 'É Impar!')
