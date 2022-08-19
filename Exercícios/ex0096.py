# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.
def área(l, c):
    a = l * c
    print(f'A área de um terreno com largura de {l} metros e comprimento de {c} metros é de {a} metros quadrados.')


# Programa principal
print('Controle de Terrenos')
print('--------------------')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)

