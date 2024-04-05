def leiaDin(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
            break
        me = int(num.count('.'))
        if me > 0:
            return float(num)
            break
        med = int(num.count(','))
        if med > 0:
            nnum = num.replace(',', '.')
            return float(nnum)
            break
        else:
            print(f'\033[1;31mErro! " {num} "  é um preço inválido!\033[m')


def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            print(f'\033[1;32m{num} é um valor Valido!\033[m')
            return int(num)
            break
        me = int(num.count('.'))
        if me > 0:
            print(f'\033[1;31mErro! " {num} "  é um valor Real, Digite um valor Inteiro!\033[m')
        else:
            print(f'\033[1;31mErro! " {num} "  Não é um valor inteiro!\033[m')


def leiareal(msg):
    while True:
        num = str(input(msg))
        me = int(num.count('.'))
        if me > 0:
            return float(num)
            print(f'\033[1;32m{num} é um valor Valido!\033[m')
            break
        med = int(num.count(','))
        if med > 0:
            nnum = num.replace(',', '.')
            print(f'\033[1;32m{nnum} é um valor Valido!\033[m')
            return float(nnum)
            break
        if num.isnumeric():
            print(f'\033[1;31mErro! " {num} "  é um valor Inteiro, Digite um valor Real!\033[m')
        else:
            print(f'\033[1;31mErro! " {num} "  é um valor inválido!\033[m')
