print('=-' * 20)
s = 0
b = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        b += 1
print('{} divisiveis por 3 deu {}'.format(b, s))




