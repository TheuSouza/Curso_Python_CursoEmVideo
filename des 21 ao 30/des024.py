cid = input('Digite o nome da sua cidade: ')
ss = (cid.upper().split()[0] == 'SANTOS')
if not ss:
    print('Sua cidade Não começa com SANTOS')
else:
    print('Sua cidade começa com SANTOS')
