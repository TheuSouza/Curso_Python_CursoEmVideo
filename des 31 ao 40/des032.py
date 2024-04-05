from datetime import date
ano = int(input('Digite o Ano (****) se quiser saber o ano atual Digite "0": '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} não é ano Bissexto'.format(ano))


