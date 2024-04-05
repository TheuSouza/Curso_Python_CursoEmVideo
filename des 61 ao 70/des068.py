from time import sleep
from random import randint
print('=-' * 20)
print(f'{"  brincando de par ou impar  ":=^40}'.upper())
print('=-' * 20)
c = 0
while True:
    cop = randint(1, 5)
    pep = int(input('De 0 a 5 - Digite um valor: '))
    paoin = str(input('Quer Par ou Ímpar [P/I]: ')).strip().upper()
    if paoin == 'I':
        if (cop + pep) % 2 == 0:
            print('--' * 20)
            print(f'Você jogou {pep}, O Computador jogou {cop}\nA soma é {cop + pep} o valor é PAR.')
            print('\033[1;31mVocê PERDEU!\033[m')
            print('--' * 20)
            sleep(0.4)
            break
        else:
            print('--' * 20)
            print(f'Você jogou {pep}, O Computador jogou {cop}\nA soma é {cop + pep} o valor é ÍMPAR.')
            print('\033[1;32mVocê GANHOU!\033[m')
            print('--' * 20)
            c += 1
    elif paoin == 'P':
        if (cop + pep) % 2 == 0:
            print('--' * 20)
            print(f'Você jogou {pep}, O Computador jogou {cop}\nA soma é {cop + pep} o valor é PAR.')
            print('\033[1;32mVocê GANHOU!\033[m')
            print('--' * 20)
            c += 1
        else:
            print('--' * 20)
            print(f'Você jogou {pep}, O Computador jogou {cop}\nA soma é {cop + pep} o valor é ÍMPAR.')
            print('\033[1;31mVocê PERDEU!\033[m')
            print('--' * 20)
            sleep(0.4)
            break
print(f'GAMER OVER!, Você vendeu {c} Vezes.')





