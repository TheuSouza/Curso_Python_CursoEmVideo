matrx = [[], [], []]
somaPar = somaterceira = maiorDois = 0
for nu in range(3):
    for cont in range(3):
        matrx[nu].append(int(input(f'Digite um valor para [{nu}, {cont}]: ')))
for nu in matrx:
    for cont in range(3):
        print(f'[ {nu[cont]:^5} ]', end='')
    print()
print(' -' * 20)