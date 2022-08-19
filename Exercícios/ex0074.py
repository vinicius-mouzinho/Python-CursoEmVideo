# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o maior e o menor valor que estão na tupla.

from random import randint

print('Vou criar uma lista com cinco números aleatórios de 1 a 100 e informarei o maior e o menor.')

lista = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print(f'Lista de números gerados aleatoriamente: {lista}')
print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')



