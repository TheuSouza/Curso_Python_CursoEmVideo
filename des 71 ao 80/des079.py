lista = []
while True:
    nu = int(input('Digite um valor: '))
    if nu not in lista:
        lista.append(nu)
        print('Valor adionado com Sucesso....')
    else:
        print(f'O valor {nu} já foi adcionado, não vou duplicar...')
    res = ' '
    while res not in 'NS':
        res = str(input('Quer continuar [S/N]: ')).strip().upper()
    if res in 'N':
        break
print('- ' * 20)
print(sorted(lista))


