# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Digite a velocidade do seu carro: '))
m = 7 * (v - 80)
if v >= 80:
    print('Você foi multado!')
    print(f'O valor da sua multa é de R$ {m:.2f}')
else:
    print('Você não foi multado.')