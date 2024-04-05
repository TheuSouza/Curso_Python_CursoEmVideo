from time import sleep
import random
print('*=' * 20)
print(f'{"  BRINCANDO DE JOKENPÔ  ":=^40}')
print('*=' * 20)
esc = int(input('[1] PEDRA \n[2] PAPEL \n[3] TESOURA \nDigite opção:'))

if esc == 1:
    esc = 'PEDRA'
elif esc == 2:
    esc = 'PAPEL'
elif esc == 3:
    esc = 'TESOURA'

lis = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(lis)
print('ANALISANDO O GANHADOR...')
sleep(1.2)
if pc == 'PAPEL' and esc == 'PEDRA' or pc == 'PEDRA' and esc == 'TESOURA' or pc == 'TESOURA' and esc == 'PAPEL':
    print('Escolhi = {}, você = {}.'.format(pc, esc))
    print('\033[1;31mVOCÊ PERDEU!!\033[m')
elif pc == 'PAPEL' and esc == 'TESOURA' or pc == 'PEDRA' and esc == 'PAPEL' or pc == 'TESOURA' and esc == 'PEDRA':
    print('Escolhi = {}, você = {}.'.format(pc, esc))
    print('\033[1;32mVOCÊ GANHOU!!\033[m')
elif pc == esc:
    print('Escolhi = {}, você também.'.format(pc))
    print('\033[7;30m Ninguem Ganhou!\033[m')













