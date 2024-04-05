nome = []
nome.append('') # Adionar itens a lista na ultima posição.
nome.insert(0,'') # Adionar na posição escolinha antes da virgula.

del nome['x'] # Deleta o item na posição determinada.
nome.pop(2) # Geralmente usado para eliminar o ultimo item, mas pode passar a posição desejada.
nome.remove('Valor') # com Remove se indica o valor dentro da lista.

lista = list(range(1, 11))

lis = [3, 5, 2, 7, 1]
print(lis)
cre = sorted(lis)
print(cre)
dec = sorted(lis, reverse=True)
print(dec)
print(sorted(lis), sorted(lis, reverse=True))


