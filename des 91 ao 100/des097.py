def msf(txt):
    medida = 4 + len(txt)
    print('~' * medida)
    print(f'  {txt}  ')
    print('~' * medida)


mensagem = str(input('Digite uma msg personalizada: '))
msf(mensagem)