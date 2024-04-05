print('CALCULANDO TINTA PARA A PINTURA')
a = float(input('Qual a Altura da Parede em Metros: '))
c = float(input('Qual o Comprimento também em Metros: '))
mq = a * c
ti = mq / 2
print('Você tem uma área total de {} Metros e vai gastar {} Litros de Tinta'.format(mq, ti))
