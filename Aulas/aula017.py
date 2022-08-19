
lista = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']

lista.insert(2, 'Cachorro-quente')
print(lista)

# lista[1] = 'Coca-cola' = muda o valor de um item da lista

'''lista.append('Cookie')''' #append = adiciona novo objeto no final da lista
'''print(lista)'''

'''lista.insert(0, 'Cachorro quente')''' #insert = insere objeto na posição indicada
'''print(lista)'''

# Métodos para deletar - eles eliminam os elementos e recontam os índices

'''del lista[3]
lista.pop(3)''' # sem especificação, elimina o último objeto
# lanche.remove('Pizza') eliminação pelo conteúdo da primeira ocorrência da lista

# Para verificar se algum item está na lista e removê-lo caso sim
'''if 'Pizza' in lista:
    lista.remove('Pizza')'''

# Cria uma lista de 4 a 10 em
'''valores = list(range(4, 11))
valores.sort()# ordena todos os valores
valores.sort(reverse=True) #ordena os valores na ordem reversa
len(valores) #mostra quantos elementos tem na lista'''

valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
# b = a isso aqui faz uma ligação entre as duas listas, o que muda em uma mudará na outra
b = a[:] # assim você faz uma cópia da lista corretamente.
b[2] = 8
print(a)
print(b)
