nome = input('Digite seu nome:')
print('Olá, prazer em te cohecer {:20}!!'.format(nome))  #nome com 20 espaço
print('Olá, Prazer em te conhecer {:>20}!!'.format(nome))  #nome alinhado a > Direta
print('Olá, Prazer em te conhecer {:<20}!!'.format(nome))  #nome alinhado a < Esquerda
print('Olá, Prazer em te conhecer {:^20}!!'.format(nome))  #nome alinhado a ^ Centralizado
print(f'Olá, Prazer em te conhecer {nome:=^20}!!')  #nome alinhado a ^ Centralizado, Resto dos espaços com =


print('Olá {},\nPrazer em te Conhecer, \nSeja bem vindo(a)'.format(nome), end=' ')  # \n Quebra a linha
print('Vamos começar ?')  # end=' ' Continua na mesma linha