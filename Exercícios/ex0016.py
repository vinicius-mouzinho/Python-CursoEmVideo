#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.


from math import trunc

print('Digite um número real e eu vou te mostrar a sua porção inteira!')
real = float(input('Digite o número real: '))
print(f'A parte inteira desse número é {trunc(real)}')


