numer = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
    'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove','Vinte')

while True:
    nu = int(input('Digite um número entre 0 e 20: '))
    if 0 <= nu <= 20:
        print(f'Você Digitou o número \033[7;32m{numer[nu]}.\033[m')
        res = str(input('Quer continuar [S/N]: ')).strip().upper()
        if res in 'N':
            break
        if res in 'S':
            print('Ok, Vamos continuar...')
        while res not in 'NS':
                print('\033[7;31mOpção incorreto...\033[m')
                res = str(input('Quer continuar [S/N]')).strip().upper()
    else:
        print('\033[7;31mValor incorreto...\033[m')





