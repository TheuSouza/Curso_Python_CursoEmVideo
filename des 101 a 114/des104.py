def leiaint(resp):
        ok = False
        valor = 0
        while True:
            num = str(input(resp))
            if num.isnumeric():
                valor = int(num)
                ok = True
            else:
                 print('\033[1;31mERRO! Digite um número inteiro valido...\033[m')
            if ok:
                break
        return valor


n = leiaint('Digite um valor: ')
print(f'você acabou de digitar o valor {n}')
