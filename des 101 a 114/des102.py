def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, - 1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} X', end=' ')
            elif c == 1:
                print(f'{c} =', end=' ')
    return f


nu = int(input('Digite um numero: '))
nu = fatorial(nu, True)
print(nu)

