carteira = []
c = 0
while True:
    carteira.append(int(input('Digite um valor: ')))
    c += 1
    re = str(input('Quer continuar [S/N]: ')).strip().upper()
    if re not in 'NS':
        print('Opção Invalida!')
        re = str(input('Quer continuar [S/N]: ')).strip().upper()
    if re in 'N':
        break
print('- ' * 20)
print(sorted(carteira, reverse=True))
print('- ' * 20)
print(f'Total de numeros digitados foi {c}.')
if 5 in carteira:
    print(f'O numero 5 foi digitado {carteira.count(5)} vezes.')
else:
    print('Não foi digitado o numero 5.')
