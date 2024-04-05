from datetime import date
from time import sleep
ana = date.today().year
print('==' * 20)
print(f'{" EXE BRASIL ":=^40}')
print('==' * 20)
ida = int(input('Qual ano você nasceu (XXXX): '))
idade = ana - ida
print('ANALISANDO...')
sleep(1.5)
if idade < 18:
    print('Você ainda vai se alistar ao serviço militar')
    print('Faltam {} Anos.'.format(18 - idade))
elif idade > 18:
    print('Você já passou do tempo de alistamento, corra e se aliste.')
    print('Já passou {} Anos'.format(idade - 18))
else:
    print('É a hora de se alistar, Não perca tempo!')

