print('CALCULANDO DESCONTO EM PRODUTOS')
pro = float(input('Digite o Valor do Produto: '))
des = float(input('Digite Quantos % de Desconto: '))
vd = pro * des / 100
vt = pro - vd
print('O Valor a ser pago agora é de {:.2f}'.format(vt))