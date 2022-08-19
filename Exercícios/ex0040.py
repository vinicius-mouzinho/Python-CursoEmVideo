# Crie um programa que leia duas notas de um aluno e calcule sua média.
# O programa deve mostrar, ao final, se ele está reprovado (nota < 5), em recuperação (6.9 >= nota >= 5.0),
# ou aprovado (nota > 7).

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2)/2

if media > 7:
    print(f'Sua média foi de {media} e você está aprovado!')
elif 6.9 >= media >= 5.0:
    print(f'Sua média foi de {media} e você está de recuperação!')
else:
    print(f'Sua média foi de {media} e você está reprovado!')