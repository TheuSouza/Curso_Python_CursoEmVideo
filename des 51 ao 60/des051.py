print(f'{" progressão aritmética ":=^40}'.upper())
print('*-' * 20)
pi = int(input('Digite o primeiro termo: '))
ra = int(input('Digite a razão: '))
dec = pi + (10 - 1) * ra
for c in range (pi, dec + ra, ra):
    print('...{:2}'.format(c), end='')






