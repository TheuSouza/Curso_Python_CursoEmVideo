print('=-' * 20)
print(f'{"  TABUADA INFINITA  ":=^40}')
print('=-' * 20)
while True:
    c = 1
    nu = int(input('Quer ver a Tabuada de qual valor: '))
    if nu < 0:
        break
    for c in range (1, 11):
        print(f'{nu} x {c:2} = {nu * c}')
    print('=-' * 20)
print('Fim do Programa.')







