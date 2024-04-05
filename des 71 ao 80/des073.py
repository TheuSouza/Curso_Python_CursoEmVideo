print('=-' * 20)
print(f'{"  brasileirinhas  ":=^40}'.upper())
print('=-' * 20)
time = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
        'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional',
        'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
        'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
for pos, t in enumerate(time):
    print(f'{pos + 1:2}º = {t:12}')
print('=-' * 20)
print('TOP 05:'.upper())
for c in range (0, 5):
    print(f'\033[1;32m     {c + 1:2}º = {time[c]}')
print('\033[m=-' * 20)
print('04 na Lantera:'.upper())
for c in range (16, len(time)):
    print(f'\033[1;31m      {c + 1:2}º = {time[c]}')
print('\033[m=-' * 20)
print('Procurando TIME:'.upper())
tt = time.index('Botafogo')
if tt >= 0:
    print(f'O {time[tt]} está na {tt + 1}º Posição.')
else:
    print('Esse time não está na tabela.')
print('=-' * 20)
print('Tabela em Ordem Alfabetica:'.upper())
for ord, g in enumerate(sorted(time)):
    print(f'{ord + 1:2}º = {g:12}')


