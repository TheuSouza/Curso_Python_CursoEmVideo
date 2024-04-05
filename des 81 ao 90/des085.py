parImpar = [[], []]
for cont in range(7):
    nu = int(input(f'Digite o {cont + 1} Valor: '))
    if nu % 2 == 0:
        parImpar[0].append(nu)
    else:
        parImpar[1].append(nu)
print(f'Numero Par {sorted(parImpar[0])}')
print(f'Numero Impar {sorted(parImpar[1])}')
