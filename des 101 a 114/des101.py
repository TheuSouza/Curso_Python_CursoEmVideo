def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade >= 65 or 16 <= idade < 18:
        return f'Com {idade} Anos seu Voto é Opcional.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos seu Voto é obrigatorio.'
    else:
        return f'Com {idade} Anos você não vota.'


while True:
    ano = str(input('Em que ano você nasceu (xxxx): '))
    if len(ano) < 4:
        print('Valor incorreto... Digite o ano com 4 digitos.')
    else:
        break

ano = int(ano)
print(voto(ano))
