# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# 999, que é a condição de parada. No final, mostre quantos números foram escritos e qual foi a soma entre eles
# (desconsiderando o flag).

n = soma = cont = 0
print('Irei calcular a soma entre todos os números que você digitar,'
      ' além de informar a soma entre eles. Digite 999 caso queira parar.')

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é {soma}')
