# Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas; B) Uma listagem com as pessoas mais pesadas; C) Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
numdepessoas = 0
maior = menor = 0
while True:
    dados.append(input('Diga o seu nome: '))
    dados.append(float(input('Diga o seu peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    numdepessoas += 1
    continuar = input('Digite "N" se deseja parar de adicionar pessoas ou qualquer outro caracter se deseja continuar: ').strip()
    if continuar in 'Nn':
        break

print(f'Os dados cadastrados foram: {pessoas}.')
print(f'Ao todo, você cadastrou {numdepessoas} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de: \n', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {menor}kg. Peso de: \n', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]')



