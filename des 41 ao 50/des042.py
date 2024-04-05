ra = float(input('Digite primeiro numero: '))
rb = float(input('Digite segundo numero: '))
rc = float(input('Digite terceiro numero: '))
rrr = (rc + rb > ra) == (rc + ra > rb) == (rb + ra > rc)
print('*-' * 22)
if rrr:
    print('Com essas medidas pode se formar um triagulo.')
    if rc == rb == ra:
        print('Esse Triangulo é EQUILATERO.')
    elif rc == rb or rc == ra or rb == ra:
        print('Esse Triangulo é ISÓSCELES.')
    else:
        print('Esse Triangulo é ESCALENO.')
else:
    print('Infelizmente não é possivel formar um triangulo.')


