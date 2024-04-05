ra = float(input('Digite primeiro numero: '))
rb = float(input('Digite segundo numero: '))
rc = float(input('Digite terceiro numero: '))
rrr = (rc + rb > ra) == (rc + ra > rb) == (rb + ra > rc)
print(rrr)
if rrr == True:
    print('Com essas medidas pode se formar um triagulo.')
else:
    print('Infelizmente não é possivel formar um triangulo.')



