print('*=' * 20)
print(f'{" LOJA 25 SEM MARÇO ":=^40}')
print('=*' * 20)
pro = float(input('Qual o valor do produto R$: '))
print('CONDIÇÕES DE PAGAMENTO:')
print('     [1] Dinheiro (10% Desconto).')
print('     [2] Cartão de Crédito.')
cond = int(input('Digite a Opção desejada: '))
conc = 0
if cond == 1:
    pro = pro - (pro * 10 / 100)
    print('Para pagamentos em Dinheiro, com Desconto de 10% o valor ficou R$:{:.2f}'.format(pro))
elif cond == 2:
    print('CONDIÇÕES NO CARTÃO DE CRÉDITO:')
    print('     [1] À Vista (5% Desconto).')
    print('     [2] Em 2 Vezes (Preço Normal).')
    print('     [3] Em 3 vezes ou mais (20% de Juros)')
    conc = int(input('Digite a Opção desejada: '))

if conc == 1:
    pro = pro - (pro * 5 / 100)
    print('Para Pagamentos em Crédito à vista, com Desconto de 5% o valor ficou R$:{:.2f}'.format(pro))
elif conc == 2:
    print('Para pagamento em 2 vezes o preço não sofre alteração, ficando o mesmo valor de R$:{:.2f}'.format(pro))
elif conc == 3:
    pro = pro + (pro * 20 / 100)
    print('Para pagamentos em 3 vezes ou mais o preço tem acressimo de 20% juros, ficando em R$:{:.2f}'.format(pro))


