from random import shuffle
lista = []
while len(lista) < 4:
    aluno = input('Digite o nome do aluno: ')
    lista.append(aluno)

shuffle(lista)
print('Ordem de Apresentação')
print(lista)
