from time import sleep
def tenInt(msg):
    while True:
        try:
            num = int(input(f'\033[1;35m - {msg}\033[m'))
        except (ValueError, NameError, TypeError):
            print(f'\033[1;31m * ERRO: não é um valor Inteiro!\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[1;34m * Usuario não digitou nenhuma opção.\033[m')
            print('\033[1;7;40m * Encerrando Programa... \033[m')
            sleep(0.5)
            return 3
        else:
            if num > 3 or num <= 0:
                print(f'\033[1;31m * ERRO: não é um Opção Valida!\033[m')
                return num
            if num == 1 or num == 2:
                print(f'\033[1;32m * {num} é um valor Válido!\033[m', end=' ')
                print('Processando...')
                sleep(0.5)
                return num
            if num == 3:
                print(f'\033[1;32m * {num} é um valor Válido!\033[m')
                print('\033[1;7;40m * Encerrando Programa... \033[m')
                sleep(0.5)
                return 3


def leiaIdade(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            print(f'\033[1;32m * {num} é uma Idade Valido!\033[m')
            return int(num)
            break
        else:
            print(f'\033[1;31m * Erro! " {num} " é uma Idade Invalida!\033[m')


