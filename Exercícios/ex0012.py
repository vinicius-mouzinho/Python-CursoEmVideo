# Crie um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Descubra o preço de um produto com nosso desconto de 5%!')
original = float(input('Insira o preço original do produto, em reais: '))
print(f'O preço novo desse produto é R$ {(original/100) * 95}!')
