# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele pretende pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então
# o empréstimo será negado.

print('Esse programa vai te informar se você pode ou não receber o nosso empréstimo.')
valor_da_casa = float(input('Qual é o valor da casa, em reais? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar essa casa? '))
prestacao_mensal = float((valor_da_casa/anos/12))

print(f'A sua prestação mensal será R$ {prestacao_mensal:.2f}.')
print(f'Você pode pagar, no máximo, R$ {salario * 0.3} de prestação mensal.')

if prestacao_mensal > salario * 0.3:
    print('O seu salário não é suficiente para esse empréstimo.')
else:
    print('O empréstimo será realizado!')   

