# Faça um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e a soma entre eles.

print('Vou calcular a soma entre todos os números que você informar'
      ' enquanto ele não for 999.')
n1 = int(input('Digite um número: '))
contagem = 0
soma = 0

while n1 != 999:
    soma += n1
    contagem += 1
    n1 = int(input('Digite um número: '))

print(f'Você digitou {contagem} números e a soma entre eles foi de {soma}')