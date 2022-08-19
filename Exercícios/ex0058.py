# Faça um programa onde o computador "pense" em um número entre 0 e 10. O jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
tentativas = 0
acertou = False
random = randint(1, 10)
print('O computador pensou em um número aleatório entre 1 e 10. Qual será...?')

while not acertou:
    chute = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if random == chute:
        acertou = True
    else:
        if chute > random:
            print('Você chutou um valor maior!')
        if chute < random:
            print('Você chutou um valor menor!')

print(f'Acertou com {tentativas} tentativas! Parabéns!')
