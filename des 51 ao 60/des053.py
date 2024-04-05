fra = str(input('Digite uma frase: ')).strip().upper()
pala = fra.split()
jun = ''.join(pala)
inv = ''
# inv = jun[::-1] mandeira de escrever voltando sem usar FOR.
for letra in range (len(jun) - 1, - 1, - 1 ):
    inv += jun[letra]
print('O inverso de {} é {}'.format(jun, inv))
if inv == jun:
    print('Essa frase é um Palíndromo.')
else:
    print('Essa frase não é Palíndromo.')






