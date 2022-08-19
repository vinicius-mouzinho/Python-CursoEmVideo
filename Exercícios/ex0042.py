# Crie um programa que leia o valor dos três lados de um triangulo e informe se é possível a sua existência.
# Além disso, o programa deve informar se o triângulo é equilátero, isósceles ou escaleno.

l1 = int(input('Digite o valor do primeiro lado do triângulo: '))
l2 = int(input('Digite o valor do segundo lado do triângulo: '))
l3 = int(input('Digite o valor do terceiro lado do triângulo: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Esse triângulo pode existir!')
else:
    print('Esse triângulo não pode existir.')

if l1 == l2 == l3:
    print('Esse triângulo é equilátero!')
elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
    print('Esse triângulo é isósceles!')
elif l1 != l2 != l3:
    print('Esse triângulo é escaleno!')

