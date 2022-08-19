# Faça um programa que leia três números e informe o maior e o menor.


print('Descubra qual de três números é o maior e o menor!')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a > b and a > c:
    print(f'O maior valor é {a}')
elif b > a and b > c:
    print(f'O maior valor é {b}')
elif c > a and c > b:
    print(f'O maior valor é {c}')

if a < b and a < c:
    print(f'O menor valor é {a}')
elif b < a and b < c:
    print(f'O menor valor é {b}')
elif c < a and c < b:
    print(f'O menor valor é {c}')
