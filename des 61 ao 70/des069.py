print('=-' * 20)
print(f'{"  cadastrando pessoas  ":=^40}'.upper())
print('=-' * 20)

c = me18 = hom = mu20 = idade = sex = 0
while True:
    c += 1
    print(f'{c}º Pessoa:')
    idade = int(input('Qual a Idade: '))
    sex = str(input('Qual sexo [M/F]: ')).strip().upper()
    if sex != 'M' and sex != 'F':
        print('\033[1;31mA opção digitada é incorreta, tente novamente.\033[m')
        sex = str(input('Qual sexo [M/F]: ')).strip().upper()
    if idade >= 18:
        me18 += 1
    if sex == 'M':
        hom += 1
    if idade < 20 and sex == 'F':
        mu20 += 1
    re = str(input('Quer continuar [S/N]: ')).strip().upper()
    if re != 'N' and re != 'S':
        print('\033[1;31mA opção digitada é incorreta, tente novamente.\033[m')
        re = str(input('Quer continuar [S/N]: ')).strip().upper()
    if re == 'N':
        break
print('=-' * 20)
print(f'Total de pessoas com mais de 18 anos foram: {me18}')
print(f'Total de homens cadastrados foram: {hom}')
print(f'Total de mulheres com menos de 20 anos foram: {mu20}')





