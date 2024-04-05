fr = str(input('Digite uma Frase: ')).strip()
print('Tem um total de {} Letras "A" nessa frase.'.format(fr.upper().count('A')))
print('A Primeira Letra "A" está na {}º Posição.'.format(fr.upper().find('A') + 1))
print('A ultima Letra apareceu na posição {}'.format(fr.upper().rfind('A') + 1))


