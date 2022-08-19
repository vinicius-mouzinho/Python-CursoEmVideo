# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.

lista = list()
lista_par = list()
lista_impar = list()
continuar = 'S'


while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    continuar = input('Deseja continuar adicionando números às listas? [S/N]: ')
    if continuar in 'Nn':
        break

print(f'A lista que você digitou é {lista}')
print(f'Os números pares são {lista_par}')
print(f'Os números ímpares são {lista_impar}')
