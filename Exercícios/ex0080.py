# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastrá-los em uma lista, já na posição
# correta de inserção (sem usar o sort). No final, mostre a lista ordenada na tela.

maior = 0
menor = 0
lista = list()

for c in range(1, 6):
    n = int(input('Digite um valor: '))
    maior = menor = n
    if c == 1 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(lista)



