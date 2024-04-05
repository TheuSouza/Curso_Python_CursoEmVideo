numer = (int(input('Digite 1º numero: ')),
         int(input('Digite 2º numero: ')),
         int(input('Digite 3º numero: ')),
         int(input('Digite 4º numero: ')))
print('--' * 20)
print(f'Você digitou os seguintes valores {numer}')
print('--' * 20)
print('O menor valor foi {}.'.format(sorted(numer)[0]))
print('O valor 9 apareceu {} veses.'.format(numer.count(9)))
if 3 in numer:
    print('O primeiro 3 apareceu na {}º posição.'.format(numer.index(3) + 1))
else:
    print('Não foi digitado nenhuma valor 3.')
print('Você digitou os seguntes numeros pares: ', end='')
for n in numer:
    if n % 2 == 0:
        print(n, end=' ')