via = int(input('Quantos KM é a viagem: '))
if via > 200:
    print('O Custo da viagem ficou em R${:.2f}'.format(via * 0.45))
else:
    print('O custo da viagem ficou em R${:.2f}'.format(via * 0.50))