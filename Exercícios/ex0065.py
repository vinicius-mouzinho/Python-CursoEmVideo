# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
# os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

soma = 0
contagem = 0
maior = 1
menor = 999999999
print('Olá! Irei calcular a média entre todos os números que você digitar!')
N = int(input('Digite um número inteiro: '))

while N != 0:
    if N > maior:
        maior = N
    if N < menor:
        menor = N
    soma = soma + N
    contagem += 1
    N = int(input('Digite um número inteiro para continuar ou 0 se deseja parar: '))

if N == 0:
    print(f'A média entre eles é {soma/contagem}')
    print(f'O menor valor digitado foi {menor} e o maior valor digitado foi {maior}.')