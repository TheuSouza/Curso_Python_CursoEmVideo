print('=-' * 20)
print(f'{"  fazendo compras  ":=^40}'.upper())
print('=-' * 20)
soma = maior = menor = menorprod = 0
while True:
    prod = str(input('Digite o nome do produto: '))
    valor = float(input('Qual o valor do produto: '))
    soma += valor
    if valor > 1000:
        maior += 1
    elif menor == 0 or valor < menor:
        menor = valor
        menorprod = prod
    res = str(input('Quer cadastrar mais produtos [S/N]: ')).strip()
    if res in 'Nn':
        break
print(f'Total gasto R$:{soma:.2f}.')
print(f'Total de produtos que custaram mais de R$:1.000,00 foram {maior} Produtos.')
print(f'O produto mais barato foi {menorprod.upper()} custando R$:{menor:.2f}.')



