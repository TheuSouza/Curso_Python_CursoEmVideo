print('\033[31m=' * 37, '\033[m')
print('\033[34m== CONVERSOR DE R$ PARA 円 e Dólar ==\033[m')
print('\033[31m=' * 37, '\033[m')
va = float(input('Quantos Reais você tem?:'))
en = va / 0.034
do = va / 4.87
print('\033[32mR$ {:.2f}\033[m Compra hoje um total de \033[35m{:.2f} 円\033[m'.format(va, en))
print('\033[32mR$ {:.2f}\033[m Compra Hoje um total de \033[35m{:.2f} Dólar\033[m'.format(va, do))
