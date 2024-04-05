matrx = [[], [], []]
somaPar = somaterceira = maiorDois = 0
for nu in range(3):
    for cont in range(3):
        matrx[nu].append(int(input(f'Digite um valor para [{nu}, {cont}]: ')))
for nu in matrx:
    for cont in range(3):
        print(f'[ {nu[cont]:^5} ]', end='')
        if nu[cont] % 2 == 0:
            somaPar += nu[cont]
        if cont == 2:
            somaterceira += nu[cont]
        if nu[cont] == matrx[1][cont]:
            if maiorDois < nu[cont]:
                maiorDois = nu[cont]
    print()
print(' -' * 20)
print(f'Soma Par {somaPar}')
print(f'Soma Terceira Coluna {somaterceira}')
print(f'Maior Valor Segunda linha {maiorDois}')


