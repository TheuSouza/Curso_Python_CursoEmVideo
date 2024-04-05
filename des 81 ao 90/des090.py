arquivo = dict()
arquivo['nome'] = str(input('Nome Aluno: '))
arquivo['média'] = float(input('Média: '))
if arquivo['média'] >= 7:
    arquivo['status'] = 'Aprovado'
else:
    arquivo['status'] = 'Reprovado'
print(f'O nome é: {arquivo['nome']}')
print(f'A média é: {arquivo['média']}')
print(f'O status é: {arquivo['status']}')
