from time import sleep
from random import randint


def sorteiro():
    numeros = list()
    print('Sorteando 5 valores: ', end='')
    for c in range(5):
        nu = randint(1, 20)
        if nu % 2 == 0:
            print(f'\033[1;32m{nu}\033[m', end='...')
        else:
            print(f'{nu}', end='...')
        sleep(0.3)
        numeros.append(nu)
    print('  \033[1;34mPronto!\033[m')
    return numeros


def somaPar(a):
    num = a
    s = 0
    print('Somando os valores pares ', end='')
    for c in num:
        if c % 2 == 0:
            print(c, end='...')
            sleep(0.3)
            s += c
    print(f'  temos {s}.')


print('- ' * 30)
print(f'{"Sortendo números":^60}')
print('- ' * 30)
liss = sorteiro()
print('- ' * 30)
somaPar(liss)