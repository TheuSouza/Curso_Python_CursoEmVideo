import math
gr = float(input('Digite a medida do angulo: '))
sr = math.radians(gr)
print('O Seno de {} = {:.4f}'.format(gr, math.sin(sr)))
print('O Cosseno de {} = {:.4f}'.format(gr, math.cos(sr)))
print('A Tangente de {} = {:.4f}'.format(gr, math.tan(sr)))

