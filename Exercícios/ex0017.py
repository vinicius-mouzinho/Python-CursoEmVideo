#Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triangulo retângulo e mostre sua hipotenusa.

'''from math import sqrt

print('Descubra o valor da hipotenusa de um triângulo retângulo!')
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h = sqrt(ca ** 2 + co ** 2)
print(f'O valor da hipotenusa é {h}')'''

from math import hypot

print('Descubra o valor da hipotenusa de um triângulo retângulo com o valor de seus catetos!')
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
h = hypot(co, ca)
print(f'O valor da hipotenusa é {h:.2f}')




