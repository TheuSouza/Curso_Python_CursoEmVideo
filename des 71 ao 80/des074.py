from random import randint
numer = (randint(1, 10), randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10))
print('Números Sorteados:')
print('--' * 20)
for n in numer:
    print(f' {n} ', end='')
print('')
print(f'O maior valor: {max(numer)}')
print(f'O menor valor: {min(numer)}')

