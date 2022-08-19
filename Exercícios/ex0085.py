#Crie um programa que leia 7 números e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

pares = list()
impares = list()
listafinal = list()

for n in range(1, 8):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

listafinal.append(sorted(pares[:]))
listafinal.append(sorted(impares[:]))
print('As listas com os valores pares e ímpares em ordem crescente são:')
print(listafinal)
