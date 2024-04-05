lista = []
for c in range(0, 5):
    nu = int(input(f'Digite o {c + 1}º Valor: '))
    if c == 0 or nu > lista[-1]:
        lista.append(nu)
    else:
        pos = 0
        while pos < len(lista):
            if nu <= lista[pos]:
                lista.insert(pos, nu)
                break
            pos += 1
print('- ' * 20)
print(lista)

