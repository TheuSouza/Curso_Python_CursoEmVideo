print('=' * 45)
print(f'{" BANCO TE METEOFUMO ":=^45}')
print('=' * 45)
imo = float(input('Qual o valor do imovel R$: '))
sal = float(input('Qual o valor do seu salario R$: '))
ano = int(input('Em quantos anos quer pagar: '))
par = imo / (ano * 12)
if sal * 30 / 100 < par:
    print('\033[1:31mEMPRESTIMO NEGADO!\033[m, Infelizmente o valor da parcela R${:.2f} excede 30% do seu R${:.2f}.'.format(par, sal))
else:
    print('\033[1:35mEMPRESTIMO APROVADO!\033[m, A parcela de R${:.2f} cabe no seu orçamento.'.format(par))
