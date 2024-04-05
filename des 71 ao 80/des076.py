lista = ('Maça', 5.3, 'Pera', 4.5, 'Melancia', 15.99, 'Banana', 6.0, 'Uva', 18.50,
         'Abacate', 8.3, 'Lichia', 13.60, 'Limão', 2.70, 'Carambola', 9.99, 'Manga', 7.80)
print('=-' * 20)
print(f'{"  lista de preços  ":=^40}'.upper())
print('=-' * 20)
for c in range (0, len(lista), 2):
    print(f'{lista[c]:.<15} R$ {lista[c + 1]:6.2f}')
print('=-' * 20)