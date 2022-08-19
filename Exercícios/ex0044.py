# Elabora um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# À vista no cartão: 5% de desconto;
# À vista dinheiro/cheque: 10% de desconto;
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros.

forma = input('Qual será a forma de pagamento? Digite 1 para à vista no dinheiro/cheque, 2 para à vista no cartão, 3 para em até 2x no cartão ou 4 para 3x ou mais no cartão: ')
if forma == 1:  