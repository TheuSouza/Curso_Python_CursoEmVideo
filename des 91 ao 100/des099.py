from time import sleep
from random import randint


def maior(* num):
    lista = num
    print('- ' * 25)
    print('Analisando valores recebidos...')
    sleep(0.5)
    for c in lista[0]:
        print(f'{c}', end='...')
        sleep(0.3)
    print('Fim...')
    if lista[0][0] == 0:
        print(f'Foi passado {max(lista[0])} valores.')
        print('Não existe nenhum valor na lista...')
    else:
        print(f'Foi passado {len(lista[0])} valores.')
        print(f'Maior valor foi {max(lista[0])}.')


liss01 = [randint(1, 10),
          randint(1, 10),
          randint(1, 10),
          randint(1, 10),
          randint(1, 10),
          randint(1, 10)]
liss02 = [randint(1, 10),
          randint(1, 10),
          randint(1, 10)]
liss03 = [randint(1, 10),
          randint(1, 10)]
liss04 = [randint(1, 10),]
liss05 = [0,]


maior(liss01)
maior(liss02)
maior(liss03)
maior(liss04)
maior(liss05)