# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9; B) Em que posição foi digitado o primeiro valor 3; C) Quais foram os números pares

lista = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))


print(f'O número 9 apareceu {lista.count(9)} vezes.')

if 3 in lista:
    print(f'O número 3 foi digitado pela primeira vez na posição {lista.index(3) + 1}')
else:
    print('O número 3 não está na lista')

print('Os valores pares digitados foram: ', end='')

for n in lista:
    if n % 2 == 0:
        print(n, end=', ')
print('Fim', end='')
