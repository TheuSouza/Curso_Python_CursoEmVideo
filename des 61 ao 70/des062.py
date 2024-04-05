print(f'{" progressão aritmética ":=^40}'.upper())
print('*-' * 20)
pi = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
c = 0
acr = 1
cont = 10
while acr != 0:
    while c < cont:
        print('{}...'.format(pi), end='')
        pi += ra
        c += 1
    print('')
    acr = int(input('Quer mostrar mais quantos Termos? '))
    cont += acr
print('Arigatouu...')



