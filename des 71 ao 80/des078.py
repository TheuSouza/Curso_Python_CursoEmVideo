lista = []
menorValor = maiorValor = 0
for c in range(0, 5):
    nu = int(input(f'Digite o {c + 1}º valor: '))
    lista.append(nu)
    if c == 0:
        menorValor = nu
        maiorValor = nu
    else:
        if menorValor > nu:
            menorValor = nu
        if maiorValor < nu:
            maiorValor = nu
print(f'Menor valor: {menorValor} Está na Posição: ', end='')
for poss, g in enumerate(lista):
    if g == menorValor:
        print(f'{poss}...', end='')
print()
print(f'Maior valor: {maiorValor} Está na Posição: ',end='')
for poss, g in enumerate(lista):
    if g == maiorValor:
        print(f'{poss}...', end='')
print()


