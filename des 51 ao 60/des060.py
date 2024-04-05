print('=-' * 20)
print(f'{"  FATORIAL  ":=^40}')
print('=-' * 20)

n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando o {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))











