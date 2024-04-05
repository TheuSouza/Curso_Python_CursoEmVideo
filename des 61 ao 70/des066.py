print('=-' * 20)
print(f'{"  CONTANDO NÚMEROS 3.0  ":=^40}')
print('=-' * 20)
c = s = 0
while True:
    nu = int(input(f'Digite o número: '))
    if nu == 999:
        break
    c += 1
    s += nu
print(f'Foram digitados um total de {c} é a soma deu {s}.')


