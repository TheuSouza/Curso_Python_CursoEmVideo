def resumo(num, acre, desc):
    print('- ' * 20)
    print(f'{"Resumo do Valor":^40}')
    print('- ' * 20)

    print(f'Preço analisado \tR$: {num:.2f}')
    print(f'Dobro do preço  \tR$: {num * 2:.2f}')
    print(f'Metade do preço \tR$: {num / 2:.2f}')
    print(f'{acre:.2f}% de aumento \tR$: {num + (num * acre) / 100:.2f}')
    print(f'{desc:.2f}% de redução \tR$: {num - (num * desc) / 100:.2f}')
    print('- ' * 20)

