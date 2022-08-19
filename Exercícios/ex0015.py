# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

print('Descubra o valor que você deve pagar!')
dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km foram rodados com o carro? '))
preco_final = 60*dias + 0.15*km
print(f'Você deve pagar R${preco_final:.2f}')

