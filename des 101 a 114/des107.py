from desafio107 import moeda

print('- ' * 40)
num = int(input('Digite um valor para ser calculado: '))
print('- ' * 40)
print(f'O dobro de R$: {num:.2f} = R$: {moeda.dobro(num):.2f}')
print(f'A metade de R$: {num:.2f} = R$: {moeda.metad(num):.2f}')
print(f'\033[1;32mAumentando 15%\033[m em R$: {num:.2f} temos = R$: {moeda.aumen(num, 15):.2f}')
print(f'\033[1;31mReduzindo 15%\033[m em R$: {num:.2f} temos = R$: {moeda.reduz(num, 15):.2f}')

