estado = dict()
brasil = list()
for c in range(3):
    estado['nome'] = str(input('Nome do Estado: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print('- ' * 20)
for e in brasil:
    for k, n in e.items():
        print(f'{k} = {n}', end=' ')
        print()
    print()
