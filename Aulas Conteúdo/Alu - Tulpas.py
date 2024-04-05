lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print('=-' * 20)
print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])
print('=-' * 20)
print(lanche[1:3])
print(lanche[1:])
print(lanche[:3])
print(lanche[-3])

print('=-' * 20)
for comi in lanche:
    print(f'Comi {comi}.')
print('=-' * 20)
for pos, comi in enumerate(lanche):
    print(f'Comi {comi:^10} na posição {pos:3}.')
print('=-' * 20)
for cont in range (0, len(lanche)):
    print(lanche[cont])
