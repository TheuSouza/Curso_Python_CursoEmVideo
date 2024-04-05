from time import sleep

print('==' * 20)
print(f'{" ESCOLA PROFESSORA DIDA ":=^40}')
print('==' * 20)
nome = str(input('Qual o nome do aluno: ')).strip()
na = float(input('Primeira nota: '))
nb = float(input('Segunda nota: '))
md = (na + nb) / 2
print('ANALISANDO MÉDIA...')
sleep(1.2)
if md < 5:
    print('A média de {} foi {}\n\033[1;31mREPROVADO!\033[m'.format(nome, md))
elif 5 <= md < 7:
    print('A média de {} foi {}\n\033[1;33mRECUPERAÇÃO!\033[m'.format(nome, md))
elif md >= 7:
    print('A média de {} foi {}\n\033[1;36mAPROVADO!\033[m'.format(nome, md))




