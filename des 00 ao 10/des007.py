print('== CALCULANDO MÉDIA DOS ALUNOS ==')
nome = str(input('Digite o nome do Aluno(a): '))
pn = float(input('Digite a primeira nota: '))
sn = float(input('Digite a Segunda nota: '))
me = (pn + sn) / 2
print('A média de {} foi {:.2f}'.format(nome, me))
