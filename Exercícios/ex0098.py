# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep


def linha():
    print('-=' * 15)


def contador():
    linha()
    print('Contagem de 1 até 10 de 1 em 1:')
    for n in range(1, 11):
        print(n, end=' ')
        sleep(0.25)
    print('FIM!')
    linha()
    print('Contagem de 10 até 0 de 2 em 2:')
    for n in range(10, -1, -2):
        print(n, end=' ')
        sleep(0.25)
    print('FIM! ')
    linha()
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if passo > 0:
        fim += 1
    if passo < 0:
        fim += -1
    for n in range(inicio, fim, passo):
        print(n, end=' ')
        sleep(0.25)
    print('FIM!')

contador()


