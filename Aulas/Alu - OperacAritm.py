import pandas
import numpy
import matplotlib

n1 = int(input('Digite Primeiro Número:'))
n2 = int(input('Digite o Segundo Número:'))
e = n1 ** n2
m = n1 * n2
d = n1 / n2
i = n1 // n2
r = n1 % n2
so = n1 + n2
su = n1 - n2
print('ORDEM DE PRECEDENCIA')
print('== 1º Posição ==')
print('Parenteses ( ) Vem sempre em Primeiro!')
print('== 2º Posição ==')
print('A Exponeciação de {} ao {} é {}.'.format(n1, n2, e))
print('== 3º Posição ==')
print('A Multiplicação entre {} e {} é {}'.format(n1, n2, m))
print('A Divisão de {} por {} é {:.2f}'.format(n1, n2, d))
print('A Divisão Inteira de {} por {} é {}'.format(n1, n2, i))
print('O Resto da Divisão de {} por {} é {}'.format(n1, n2, r))
print('== 4º Posição ==')
print('A Soma de {} e {} é {}'.format(n1, n2, so))
print('A Subtração entre {} e {} é {} '.format(n1, n2, su))

