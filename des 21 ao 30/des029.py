kmh = int(input('Estava a quantos KM/h :'))
mu = (kmh - 80) * 7
if kmh > 80:
    print('Você foi Multa! \nO valor da Multa é de R${:.2f}'.format(mu))
else:
    print('Tudo OK, Estava dentro do Limite de Velocidade.')

