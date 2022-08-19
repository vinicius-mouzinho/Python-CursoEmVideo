# Faça um programa que leia o peso de cinco pessoas e diga quem possui o maior e o menor.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'O peso da pessoa número {p} é: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg e o menor foi de {menor}kg.')
