print('== LOCALIZA CAR ==')
km = float(input('Digite Quantos KM foi percorrido com o veículo: '))
dia = int(input('Quantos dias o cliente ficou com o veículo: '))
vkm = km * 0.15
vdia = dia * 60
alu = vkm + vdia
print('Valor total a ser pago da locação é R${:.2f}'.format(alu))
