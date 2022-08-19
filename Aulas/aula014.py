# c = 1
#
# while c < 10:
#     print(c)
#     c = c + 1
# print('Fim')

# n = 1
# while n != 0:
#     n = int(input('Digite um número: '))
# print('Fim')

#r = 'S'
#while r == 'S':
 #   n = int(input('Digite um valor: '))
 #   r = input('Quer continuar? [S/N]: ').upper()
#print('Fim')

n = 1
pares = 0
impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 and n != 0:
        pares += 1
    if n % 2 != 0:
        impares += 1
print(f'Números pares digitados: {pares}')
print(f'Números ímpares digitados: {impares}')

