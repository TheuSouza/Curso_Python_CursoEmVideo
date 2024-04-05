from random import randint
from time import sleep
print('VAMOS BRINCAR!')
print('-'* 20)
print('Pensei em um número de 1 a 5, será que você acerta?')
pe = randint(1, 5)
nu = int(input('Digite o número que você escolher: '))
print('PROCESSANDO...')
sleep(1.5)
if nu == pe:
    print('PARABÉNS VOCÊ ACERTOU!!')
else:
    print('INFELIZMENTE VOCÊ ERROU.')
print('Eu pensei em {} e você escolher {}'.format(pe, nu))
