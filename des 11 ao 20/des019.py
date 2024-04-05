import random
aa = str(input('Nome Primeiro Aluno: '))
bb = str(input('Nome Segundo Aluno: '))
cc = str(input('Nome Terceiro Aluno: '))
dd = str(input('Nome Quarto Aluno: '))
sor = [aa, bb, cc, dd]
print('O Aluno sorteado foi {}'.format(random.choice(sor)))


