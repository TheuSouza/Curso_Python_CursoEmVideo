from datetime import date
from time import sleep
hoje = date.today().year
banco = dict()

banco['Nome'] = str(input('Nome: '))
banco['Idade'] = int(input('Ano de Nascimento: '))
carTrabalho = int(input('Nº Carteira de Trabalho: '))
if carTrabalho == 0:
    banco['Carteira de Trabalho'] = carTrabalho
    banco['Idade'] = hoje - banco['Idade']
else:
    banco['Carteira de Trabalho'] = carTrabalho
    banco['Contratação'] = int(input('Ano de Contratação: '))
    banco['Salário'] = float(input('Salário R$: '))

if banco['Carteira de Trabalho'] > 0:
    trabalhado = hoje - banco['Contratação']
    idadeApos = ((35 - trabalhado) + hoje) - banco['Idade']
    anoApos = (35 - trabalhado) + hoje
    banco['Idade'] = hoje - banco['Idade']
    banco['Ano de Aposentadoria'] = anoApos
    banco['Aposentar com Idade'] = idadeApos

print('- ' * 20)
print('{:^40}'.format(' COLETANDO DADOS '))
print('- ' * 20)
for da in banco.items():
    print(f'{da[0]} : \033[1;32m{da[1]}\033[m')
    sleep(0.5)
print('- ' * 20)









