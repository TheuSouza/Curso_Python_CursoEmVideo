from random import randint
from time import sleep
print('-.' * 20)
print(f'{" Palpite MEGA SENA ":^40}'.upper())
print('.-' * 20)
palpites = list()
criando = list()
jogo = 0
numJogo = int(input('Precisa de quantos jogos? '))
while jogo < numJogo:
    while 6 > len(criando):
        nu = randint(1, 60)
        if nu not in criando:
            criando.append(nu)
    palpites.append(criando[:])
    criando.clear()
    jogo += 1
cont = 1
for palp in palpites:
    print(f'{cont}º Jogo: {sorted(palp)} ')
    sleep(0.5)
    cont += 1
print(f'{" boa sorte ":-^30}'.upper())
