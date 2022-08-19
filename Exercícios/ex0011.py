#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

h = float(input('Qual é a altura da parede, em metros? '))
l = float(input('Qual é a largura da parede, em metros? '))
print(f'A área da parede é {float(h * l)} m²')
print(f'Dessa forma, a quantidade de tinta necessária para pintá-la é de {float((h * l) / 2 )} litros.')


