mas = 0
fem = 0
r = ''
while r != 'FIM':
    r = str(input('Digite seu sexo [M/F] e "FIM" para encerrar: ')).upper().strip()
    if r == 'M':
        mas += 1
    elif r == 'F':
        fem += 1
    elif r == 'FIM':
        print('\033[34mObrigado, Até Mais.\033[m')
    elif r != 'M' or r != 'F':
        print('\033[31mOpção errada, Digite uma opção valida:\033[m ')
print('=-' * 20)
print('Total de {} Pessoas do sexo Masculino'.format(mas))
print('Total de {} Pessoas do sexo feminino.'.format(fem))







