def msg(txt):
    print('- ' * 20)
    print(f'{txt:^40}'.upper())
    print('- ' * 20)


def mq(a, b):
    q = a * b
    print(f'A área do terreno {a} x {b} é = {q}')


msg('terreno M²')

largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

mq(largura, comprimento)
