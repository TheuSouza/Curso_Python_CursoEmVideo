nu = int(input('Digite um numero de 0 a 9999: '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print('UNIDADE:{}'.format(u))
print('DEZENA:{}'.format(d))
print('CENTENA:{}'.format(c))
print('MILHAR:{}'.format(m))

