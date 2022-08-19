# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

a = random.randint(1, 5)

n = int(input('Digite um número de 1 a 5: '))
if n == a:
    print('Parabéns, você acertou!')
else:
    print('Você errou!')

