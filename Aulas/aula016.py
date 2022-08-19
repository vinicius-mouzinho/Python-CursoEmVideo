# TUPLAS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')  # Para obter o lanche e sua posição

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
print(c.index(2, 4))  # Primeira posição do número 2 a partir da posição 4

pessoa = ('Gustavo', 39, 'M', 99.88) #Tupla pode receber número e string
# del(pessoa[0]) => erro pois não dá pra apagar apenas um item de uma tupla
del(pessoa)
print(pessoa)  # vai dar erro pq deletamos a pessoa
