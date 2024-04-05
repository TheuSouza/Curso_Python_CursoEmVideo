from lib import face, arquivo, valid

arq = 'cursoemvideo.txt'

if not arquivo.arqExiste(arq):
    arquivo.arqCriar(arq)

while True:
    res = face.menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Sistema'])
    if res == 3:
        break
    if res == 1:
        arquivo.arqLer(arq)
    if res == 2:
        face.cabeçalho('novo cadastro')
        nome = str(input('Nome: '))
        idade = valid.leiaIdade('Idade: ')
        arquivo.registro(arq, nome, idade)


