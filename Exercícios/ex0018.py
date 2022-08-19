#Crie um programa que mostre o seno, o cosseno e a tangente do ângulo desejado.

import math
angulo = float(input('Digite o valor de um ângulo e eu revelarei o seu seno, cosseno e tangente: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O seno deste ângulo é {seno:.2f} \nO cosseno deste ângulo é {cosseno:.2f} \ne a tangente é {tangente:.2f}')








