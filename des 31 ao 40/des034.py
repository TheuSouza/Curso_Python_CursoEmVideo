sal = float(input('Digite o salário do funcionario em R$: '))
if sal > 1250:
    sal = (sal * 10 / 100) + sal
    print('O novo salario é de R${:.2f}'.format(sal))
else:
    sal = (sal * 15 / 100) + sal
    print('O novo salario é de R${:.2f}'.format(sal))
