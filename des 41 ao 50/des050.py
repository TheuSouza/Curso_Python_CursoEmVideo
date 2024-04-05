s = 0
d = 0
for c in range (0, 6):
    nu = int(input('Digite um número: '))
    if nu % 2 == 0:
        s += nu
        d += 1
print('Total de numeros pares foi  {} e a soma {}'.format(d, s))
