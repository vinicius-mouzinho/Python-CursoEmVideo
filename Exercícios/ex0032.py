# Crie um programa que leia um ano e determine se ele é ou não bissexto

ano = int(input("Informe um ano: "))
if ((ano % 4) == 0) and ((ano % 1000) != 0):
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')