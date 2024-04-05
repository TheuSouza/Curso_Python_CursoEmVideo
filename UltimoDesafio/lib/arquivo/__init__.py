from UltimoDesafio.lib.face import cabeçalho


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arqCriar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'\033[1;37mArquivo {nome} criado com Sucesso!\033[m')


def arqLer(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        cabeçalho('pessoas cadastradas')
        for info in a:
            dado = info.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} Anos')
    finally:
        a.close()


def registro(arg, nome='desconhecido', idade=0):
    try:
        a = open(arg, 'at')
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome} ; {idade}\n')
        except:
            print('Erro ao registrar nova pessoa!')
        else:
            print(f'\033[1;37mRegistro de {nome}, Feito com sucesso!\033[m')
            a.close()
