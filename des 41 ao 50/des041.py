from datetime import date
print('*=' * 20)
print(f'{" NATAÇÃO 2.0 ":=^40}')
print('=*' * 20)
anoa = date.today().year
nasc = int(input('Qual o ano de nascimento com **** Digitos: '))
idade = anoa - nasc
if idade < 10:
    print('Categoria MIRIM até 9 Anos.')
elif 9 < idade < 15:
    print('Categoria INFANTIL de 10 a 15 Anos.')
elif 14 < idade < 20:
    print('Categoria JUNIOR de 14 a 19 Anos.')
elif idade == 20:
    print('Categoria SÊNIOR até 20 Anos.')
else:
    print('Categoria MASTER acima de 20 Anos.')


