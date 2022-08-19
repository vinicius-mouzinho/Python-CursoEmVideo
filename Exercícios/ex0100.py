# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
números = []


def sorteia():
    for n in range(1, 6):
        num = randint(1, 11)
        números.append(num)
    print(f'A lista de 5 números gerada é: {números}')


def somapar():
    somaPar = 0
    for n in números:
        if n % 2 == 0:
            somaPar += n
    print(f'A soma entre os números pares da lista é {somaPar}')




# Programa Principal:
sorteia()
somapar()
