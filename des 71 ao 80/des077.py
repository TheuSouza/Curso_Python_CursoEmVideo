palavras = ('casa', 'carro', 'celular', 'computador', 'linguagem', 'nihongo', 'banana', 'abacate',
            'feijao', 'arroz', 'sorvete', 'mouse', 'teclado', 'monitor', 'cadeira', 'mesa', 'cama')
print('--' * 20)
for cont in range(0, len(palavras)):
    print('Na palavra {:.^12} temos: '.format(palavras[cont].upper()), end='')
    for c in range(0, len(palavras[cont])):
        if palavras[cont][c] in 'aeiou':
            print(f'{palavras[cont][c]}'.upper(), end=' ')
    print('')
print('--' * 20)
for pa in palavras:
    print(f'Na palavra {pa:.^12} temos: ', end=' ')
    for le in pa:
        if le in 'aeiou':
            print(le, end=' ')
    print('')
print('--' * 20)




