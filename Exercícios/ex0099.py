# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
números = []


def maior(* núm):
    print('-=' * 30)
    print("Analisando os valores passados...")
    for n in range(1, randint(1, 10)):
        números.append(randint(1, 9))
    números.sort()
    print(f'A lista gerada foi {números}: {len(números)} números ao todo.')
    print(f'O maior número gerado na lista foi {números[-1]}')


# Programa principal

maior()
maior()
maior()
maior()
