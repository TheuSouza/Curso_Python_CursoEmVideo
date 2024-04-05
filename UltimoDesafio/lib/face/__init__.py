from UltimoDesafio.lib import valid

def linha(l=30):
    return '-' * l


def cabeçalho(msg):
    print(linha(40))
    print(f'{msg:^40}'.upper())
    print(linha(40))


def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for i in lista:
        print(f'\033[1;7;35m {c} \033[m - {i}')
        c += 1
    print(linha(40))
    opc = valid.tenInt('Digite sua opção: ')
    return opc
