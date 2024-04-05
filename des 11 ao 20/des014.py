gc = float(input('Qual a temperatura em Graus ºC: '))
gf = gc * 1.8 + 32
print('{}ºC em Fahrenheit é {:.1f}ºF'.format(gc, gf))

gff = float(input('Qual a temperatuda em Graus ºF: '))
gcc = (gff - 32) / 1.8
print('{}ºF em Celsius é {:.1f}ºC'.format(gff, gcc))

