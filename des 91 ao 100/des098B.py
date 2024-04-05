from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= - 1
    if p == 0:
        p = 1
    print('- ' * 20)
    print(f'Contadem de {i} até {f} de {p} em {p}.')
    sleep(0.4)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= p
        print('Fim!')


print('- ' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
