from time import sleep
from operator import neg


def contador(inicio, fim, passo):
    if inicio < fim:
        if passo <= 0:
            passo = 1
        print('==' * 20)
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
        print('- ' * 20)
        for c in range(inicio, fim + 1, passo):
            print(f'{c}', end=' ')
            sleep(0.3)
        print('Fim!')
    if inicio > fim:
        if passo == 0:
            passo = - 1
        print('==' * 20)
        if passo < 0:
            print(f'Contando de {inicio} até {fim} de {neg(passo)} em {neg(passo)}')
        else:
            print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
        print('- ' * 20)
        if passo > 0:
            passo = neg(passo)
        for c in range(inicio, fim - 1, passo):
            print(f'{c}', end=' ')
            sleep(0.3)
        print('Fim!')


contador(1, 10, 1)
contador(10, 1, 1)
print('==' * 20)
print('Agora é a sua vez!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

