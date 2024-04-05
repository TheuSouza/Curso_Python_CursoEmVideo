lista = list()
lista.append('Matheus')
lista.append(28)

nos = list()
nos.append(lista[:])  # Cria uma copia do valor na outra lista, alterando a primeira nao altera a segunda.

lista[0] = 'João'
lista[1] = 14

nos.append(lista[:])  # Cria uma copia do valor na outra lista, alterando a primeira nao altera a segunda.
print(f'sem relação {nos}')

