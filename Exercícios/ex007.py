# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Qual foi a primeira nota do aluno? '))
n2 = float(input('Qual foi a segunda nota do aluno? '))
media = (n1 + n2) / 2
if media <= 10:
    print(f'A média desse aluno é {float(media)}')
else:
    print('Apenas digite notas com valores, ao máximo, de 10')
