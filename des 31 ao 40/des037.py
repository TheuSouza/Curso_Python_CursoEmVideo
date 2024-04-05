nu = int(input('Digite um numero qualquer: '))
print('QUAL BASE DE CONVERÇÃO QUER USAR: \n[1] para Binário \n[2] para octal \n[3] Hexadecimal')
ba = int(input('Digite a opção: '))
if ba == 1:
    bi = str(bin(nu)[2:])
    print('Em Binário é : {}'.format(bi))
elif ba == 2:
    oc = str(oct(nu)[2:])
    print('Em Octal é : {}'.format(oc))
elif ba == 3:
    he = str(hex(nu)[2:])
    print('Em Hexadecimal é :{}'.format(nu))
else:
    print('\033[31mOpção Invalida!\033[m')



