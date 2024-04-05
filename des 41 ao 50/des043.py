print('*=' * 20)
print(f'{" Calculando IMC ":=^40}')
print('=*' * 20)

alt = float(input('Digite sua altura em Metros: '))
pes = float(input('Digite seu peso em Kg: '))

imc = pes / alt ** 2
if 18.5 > imc == 18.5:
    print('Faixa ABAIXO DO PESO, o IMC = {:.2f}'.format(imc))
elif 18.5 < imc < 25:
    print('Faixa PESO IDEA, o IMC = {:.2f}'.format(imc))
elif 25 == imc < 30:
    print('Faixa SOBREPESO, o IMC = {:.2f}'.format_map(imc))
elif 30 == imc < 40:
    print('Faixa OBESIDADE, o IMC = {:.2f}'.format(imc))
else:
    print('Faixa OBESIDADE MÓRBIDA, o IMC = {:.2f}'.format(imc))




