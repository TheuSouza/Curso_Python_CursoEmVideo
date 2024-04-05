print('=-' * 20)
print(f'{"  SEQUENCIA DE FIBONACCI  ":=^40}')
print('=-' * 20)
c = 2
fi = 0
bi = 1
tr = 0
ate = int(input('Até onde vai a sequencia: '))
print('{}...'.format(fi), end='')
print('{}...'.format(bi), end='')
while c < ate:
    tr = fi + bi
    print('{}...'.format(tr), end='')
    fi = bi
    bi = tr
    c += 1


