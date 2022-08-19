# Crie um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
# para viagens de até 200km e R$ 0,45 por km para viagens mais longas.

print('Descubra o preço da sua viagem!')
d = int(input('Qual a distância da sua viagem, em km? '))
if d > 200:
    print(f'O valor da sua viagem é de R$ {d * 0.45:.2f}')
else:
    print(f'O valor da sua viagem é de R$ {d * 0.50:.2f}')