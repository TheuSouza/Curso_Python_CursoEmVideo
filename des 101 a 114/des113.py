from desafio107 import lendo

# Modelo validando com funcão
num1 = lendo.leiaint('Digite um valor inteiro: ')
num1 = lendo.leiareal('Digite um valor Real: ')




# Modelo usando Try
try:
    num = int(input('\033[7;30;45m Digite um valor Inteiro: \033[m'))
except (ValueError, NameError):
    print(f'\033[1;31m * ERRO: não é um valor Inteiro!\033[m')
except KeyboardInterrupt:
    print()
    print('\033[1;34m * Usuario não digitou nenhum valor.\033[m')
else:
    print(f'\033[1;32m * {num} é um valor Válido!\033[m')
finally:
    print('\033[1;36mVolte Sempre!\033[m')


try:
    nuu = float(input('\033[7;30;45m Digite um valor Real: \033[m').replace(',', '.'))
except (ValueError, NameError):
    print(f'\033[1;31m * ERRO: não é um valor Inteiro!\033[m')
except KeyboardInterrupt:
    print()
    print('\033[1;34m * Usuario não digitou nenhum valor.\033[m')
else:
    print(f'\033[1;32m * {nuu} é um valor Válido!\033[m')
finally:
    print('\033[1;36mVolte Sempre!\033[m')