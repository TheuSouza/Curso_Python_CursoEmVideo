no = str(input('Digite seu nome completo: ')).strip()
me = no.split()
print('Maiusculo: {}'.format(no.upper()))
print('Minusculo: {}'.format(no.lower()))
print('Total de Letras é {}'.format(len(no) - no.count(' ')))
print('Seu primeiro nome {} tem {} Letras'.format(no, len(me[0])))



