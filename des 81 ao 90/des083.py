exp = str(input('Digite uma expressão: ')).strip()
cont1 = exp.count('(')
cont2 = exp.count(')')
if cont1 != cont2:
    print('Essa expressão esta incorreta.')
else:
    print('Essa expressao esta correta.')
