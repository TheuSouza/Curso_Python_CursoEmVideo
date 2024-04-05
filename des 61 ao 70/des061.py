print(f'{" progressão aritmética ":=^40}'.upper())
print('*-' * 20)
pi = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
c = 0
while c < 10:
    print('{}...'.format(pi), end='')
    pi += ra
    c += 1



