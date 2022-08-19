# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
# mostre uma listagem de preços, organizando os dados de forma tabular.

lista = ('Iogurte Whey Protein', 9.69,
         'Miojo', 2.69,
         'Queijo minas', 29.15,
         'Uva sem semente 250g', 4.99)

print('-' * 20)
print('LISTAGEM DE PREÇOS')
print('-' * 20)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]}')
