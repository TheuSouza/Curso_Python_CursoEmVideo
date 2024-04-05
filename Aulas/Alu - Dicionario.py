filmes = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'}
print('==' * 30)
print(filmes)
print(filmes.values())
print(filmes.keys())
print(filmes.items())
print('==' * 30)
for ke, va in filmes.items():
    print(f'{ke} é {va}.')
