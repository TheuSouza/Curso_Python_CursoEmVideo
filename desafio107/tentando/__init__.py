def tenInt():
    while True:
        try:
            num = int(input('\033[7;30;45m Digite um valor Inteiro: \033[m'))
        except (ValueError, NameError):
            print(f'\033[1;31m * ERRO: não é um valor Inteiro!\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[1;34m * Usuario não digitou nenhum valor.\033[m')
            return 0
        else:
            print(f'\033[1;32m * {num} é um valor Válido!\033[m')
            return num


def tenReal():
    while True:
        try:
            nuu = float(input('\033[7;30;45m Digite um valor Real: \033[m').replace(',', '.'))
        except (ValueError, NameError):
            print(f'\033[1;31m * ERRO: não é um valor Inteiro!\033[m')
        except KeyboardInterrupt:
            print()
            print('\033[1;34m * Usuario não digitou nenhum valor.\033[m')
            return 0
        else:
            print(f'\033[1;32m * {nuu} é um valor Válido!\033[m')
            return nuu

