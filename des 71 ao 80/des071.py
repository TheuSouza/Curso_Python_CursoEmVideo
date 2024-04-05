print('=-' * 20)
print(f'{"  BANCO TAMOSPARA TEFUDER  ":=^40}'.upper())
print('=-' * 20)
while True:
    print('NOTAS DISPONIVEIS:\n\033[1;32mR$50,00 R$20,00 R$10,00 R$1,00\033[m')
    saque = int(input('QUANTO QUER SACAR R$: '))
    no5 = saque // 50
    print('NOTAS:')
    if no5 == 0:
        print('', end='')
    else:
        print(f'{no5:.0f} de R$:50,00')
    no2 = saque % 50 // 20
    if no2 == 0:
        print('', end='')
    else:
        print(f'{no2:.0f} de R$:20,00')
    no1 = (saque % 50) % 20 // 10
    if no1 == 0:
        print('', end='')
    else:
        print(f'{no1:.0f} de R$:10,00')
    no = ((saque % 50) % 20) % 10 // 1
    if no == 0:
        print('', end='')
    else:
        print(f'{no:.0f} de R$:1,00')
    break
print('Volte Sempre!...')
