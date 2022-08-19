# Crie um programa que vai ler vários números e colocá-los em uma lista. Depois disso, mostre: A) Quantos números foram
# digitados; B) A lista de valores, ordenada de forma decrescente; C) Se o valor 5 foi digitado e está ou não na lista.


lista = list()
continuar = 'S'

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    print('-' * 30)
    continuar = input('Deseja continuar adicionando valores à lista? [S/N]: ')
    print('-' * 30)
    if continuar in 'Nn':
        break

print(f'Foram digitados {len(lista)} números nessa lista.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
if 5 not in lista:
    print('O valor 5 não está na lista.')
