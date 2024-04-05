def msg(txt):
    print('- ' * 20)
    print(f'{txt:^40}'.upper())
    print('- ' * 20)


def cont(* num):
    quant = len(num)
    print(f'Recebi {num} Total de {quant} números.')


def dobro(listagem):
    pos = 0
    while pos < len(listagem):
        listagem[pos] *= 2
        pos += 1


msg('Aprendendo Funções')
listagem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cont(1, 2, 3, 4, 5, 6, 7, 8, 9)
dobro(listagem)
print(f'Dobrando os valores {listagem}')