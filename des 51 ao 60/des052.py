print(f'{" número primo ":=^40}'.upper())
print('*-' * 20)
tot = 0
no = int((input('Digite um número: ')))
for c in range (1, no + 1):
    if no % c == 0:
        print('\033[1;33m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(no, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')




