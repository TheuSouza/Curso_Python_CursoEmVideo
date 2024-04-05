from desafio107 import moeda
from desafio107 import form

print('- ' * 40)
num = int(input('Digite um valor para ser calculado: '))
aumen = float(input('Acressimo: '))
desco = float(input('Desconto: '))
print('- ' * 40)
print(f'O dobro de R$: {form.form(num)} = R$: {form.form(moeda.dobro(num))}')
print(f'A metade de R$: {form.form(num)} = R$: {form.form(moeda.metad(num))}')
print(f'\033[1;32mAumentando {form.form(aumen)}%\033[m em R$: {form.form(num)} '
      f'temos = R$: {form.form(moeda.aumen(num, aumen))}')
print(f'\033[1;31mReduzindo {form.form(desco)}%\033[m em R$: {form.form(num)} '
      f'temos = R$: {form.form(moeda.reduz(num, desco))}')


