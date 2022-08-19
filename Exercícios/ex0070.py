# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre: A) Qual é o total gasto na compra; B) Quantos produtos custam mais de R$ 1000 C) Qual é o nome do
# produto mais barato.

continuar = 'S'
total_gasto = 0
produtos_caros = 0
preco_produto_barato = 999
nome_produto_barato = ''

print('CARRINHO DO CARREFOUR')

while True:
    if continuar in 'Ss':
        nome = input('Digite o nome do produto que deseja adicionar: ')
        preco = float(input('Digite o preço desse produto, em reais: '))
        print('-' * 40)
        print(f'{nome} de R$ {preco:.2f} adicionado ao carrinho com sucesso! ')
        print('-' * 40)
        total_gasto += preco
        if preco > 1000:
            produtos_caros += 1
        if preco < preco_produto_barato:
            preco_produto_barato = preco
            nome_produto_barato = nome
        continuar = input('Deseja continuar comprando? [S/N]: ')
        print('-' * 40)
    if continuar in 'Nn':
        break
print(f'O total gasto nessa compra foi de R${total_gasto}')
print(f'Você comprou {produtos_caros} produtos que custam mais de R$ 1000,00')
print(f'O nome do produto mais barato adicionado é {nome_produto_barato}, que custa R$ {preco_produto_barato}')