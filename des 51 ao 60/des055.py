mi = 0
mx = 0
for c in range(1, 6):
    pes = float(input('Digite seu peso em Kg: '))
    if c == 1:
        mi = pes
        mx = pes
    else:
        if pes > mx:
            mx = pes
        elif pes < mi:
            mi = pes
print('''O MENOR PESO FOI: {:.2f}Kg
O MAIOR PESO FOI: {:.2f}Kg'''.format(mi, mx))





