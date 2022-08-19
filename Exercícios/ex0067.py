# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('Vou mostrar a tabuada do número desejado, enquanto você não me informar um número negativo.')

while True:
    n = int(input('Deseja ver a tabuada de que valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n * c}')

