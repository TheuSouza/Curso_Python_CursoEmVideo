from time import sleep


def tituloverde(txt):
    med = len(txt) + 4
    print('\033[7;32m- ' * med)
    print(f'  {txt}  ')
    print('- ' * med)
    print('\033[m')


def tituloazul(txt):
    med = len(txt) + 4
    print('\033[7;35m- ' * med)
    print(f'  {txt}  ')
    print('- ' * med)
    print('\033[m')


while True:
    tituloverde('Sistema de ajuda PyHelp!')
    res = str(input('\033[1;7;40m Função ou Biblioteca > \033[m ')).lower()
    if res in 'fim':
        break
    tituloazul(f'Acessando o manual do comando {res}')
    sleep(0.6)
    help(res)

