from random import randint
from time import sleep
from operator import itemgetter
dado = dict()
lista = list()
for c in range(1, 5):
    sor = randint(1, 6)
    lista.append(sor)
    dado[c] = lista.copy()
    lista.clear()
ranking = list()
print('- ' * 22)
print(f'{"Sorteiro de Dados":^44}'.upper())
print('- ' * 22)
for i in dado.items():
    print(f'Jogador Nº{i[0]} Tirou: {i[1]}')
    sleep(0.3)
print('- ' * 22)
print(f'{"Ranking de Pontos":^44}'.upper())
print('- ' * 22)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
for j in ranking:
    print(f'O Jogador Nº{j[0]} Tirou {j[1]}.')
    sleep(0.3)
print('- ' * 22)







