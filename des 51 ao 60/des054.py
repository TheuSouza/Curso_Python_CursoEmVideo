from datetime import date
atu = date.today().year
ma = 0
me = 0
for c in range (0, 7):
    ano = int(input('Qual o Ano em que nasceu XXXX: '))
    if atu - ano >= 21:
        ma += 1
    elif atu - ano < 21:
        me += 1
print('Quantidade de Menor de Idade foi {}'.format(me))
print('Quantidade de Maiores de Idade foi {}'.format(ma))




