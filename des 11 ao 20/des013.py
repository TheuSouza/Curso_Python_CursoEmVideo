print('== Aumentando Salários ==')
sal = float(input('Digite o Valor do Salário: '))
aum = sal * 15 / 100
nsal = sal + aum
print('O novo Salário é de R${:.2f} teve um aumento de R${:.2f}, Parabéns!'.format(nsal, aum))
