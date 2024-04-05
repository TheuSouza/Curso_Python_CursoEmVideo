from random import randint
from time import sleep
print('=-' * 20)
print(f'{"  VAMOS BRINCAR  ":=^40}')
print('=-' * 20)
pes = randint(1, 10)
chut = 0
c = 1
print(f'{"  PENSEI EM UM NUMERO DE 1 A 10  ":=^40}')
print(f'{"  SERÁ QUE VOCE ACERTA!?  ":=^40}')
print('=-' * 20)
while chut != pes:
    chut = int(input('Qual seu {}º chute? '.format(c)))
    print('\033[7;30mPROCESSANDO...\033[m')
    sleep(0.4)
    if chut != pes:
        print('\033[1;31mErrouuuuuuuu....! Tente novamente.\033[m')
    elif chut == pes:
        print('\033[1;32m ☺ Parabéns você ACERTOU!\033[m \nPrecisou de {} Tentativas.'.format(c))
    c += 1
print('Obrigado Pelo Jogo!')








