print('=' * 30)
print(f'{" COMPARANDO VALORES! ":=^30}')
print('=' * 30)
na = float(input('Digite primeiro valor: '))
nb = float(input('Digite segundo valor: '))
if na > nb:
    print('O primeiro valor {} é maior que {}'.format(na, nb))
elif nb > na:
    print('O segundo valor {} é maior que {}'.format(nb, na))
else:
    print('Não exite valor maior {} é igual a {}'.format(na, nb))
