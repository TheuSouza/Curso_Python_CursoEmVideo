pessoas = [['João', 14], ['Matheus', 28], ['Pedro', 15], ['Lene', 49]]
#print(pessoas[1][1])
#print(pessoas[2])

galera = list()
dado = list()
print('- ' * 20)
print('- ' * 20)
for d in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print('- ' * 20)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')
print('- ' * 20)
