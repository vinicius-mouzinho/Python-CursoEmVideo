# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('Olá! Eu sou um caixa eletrônico!')
valor = int(input('Digite a quantia de dinheiro que você deseja sacar, em reais: '))

notascinquenta = valor // 50
notasvinte = (valor - (notascinquenta * 50)) // 20
notasdez = (valor - (notascinquenta * 50) - (notasvinte * 20)) // 10
notasum = (valor - (notascinquenta * 50) - (notasvinte * 20) - (notasdez * 10))
print('Saque feito com sucesso! Você irá receber a seguinte quantia de cédulas:')
print(f'{notascinquenta} cédulas de R$ 50.00')
print(f'{notasvinte} cédulas de R$ 20.00')
print(f'{notasdez} cédulas de R$ 10.00')
print(f'{notasum} cédulas de R$ 1.00')