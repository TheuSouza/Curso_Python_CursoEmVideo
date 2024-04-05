print('=-' * 20)
print(f'{"  TRBALHANDO COM NÚMEROS  ":=^40}')
print('=-' * 20)
res = 0
na = 0
nb = 0
while res != 5:
    na = float(input('Digite Primeiro Número: '))
    nb = float(input('Digite Segundo Número: '))
    res = 0
    while res != 4 and res != 5:
        print('=-' * 20)
        print('[1] Somar.')
        print('[2] Mutiplicar.')
        print('[3] Maior.')
        print('[4] Digitar Novos Números.')
        print('[5] Sair do Programa.')
        print('=-' * 20)
        res = int(input('Digite uma opção: '))
        print('=-' * 20)
        if res == 1:
            print('{} + {} = {}.'.format(na, nb, na + nb))
        elif res == 2:
            print('{} x {} = {}.'.format(na, nb, na * nb))
        elif res == 3:
            if na > nb:
                print('{} é Maior.'.format(na))
            elif nb > na:
                print('{} é Maior.'.format(nb))
            else:
                print('{} e {} São Iguais.'.format(na, nb))
print('Fim do Programa...')


