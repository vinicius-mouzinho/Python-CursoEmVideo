# Escreva um programa que compare dois números e informe se o primeiro é maior, o segundo é maior ou se são iguais.

print('Digite dois números e eu informarei qual é o maior.')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if n1 > n2:
    print(f'{n1} é maior do que o {n2}')
elif n2 > n1:
    print(f'{n2} é maior do que o {n1}')
elif n1 == n2:
    print(f'{n1} e {n2} são iguais.')
