# Escreva um programa que leia um número N inteiro e mostre na tela os N
# primeiros elementos de uma sequencia de fibonnaci.

N = int(input('Quantos números da sequência de fibonnaci você deseja ver? '))
t1 = 0
t2 = 1
print(f'{t1}, {t2}, ', end='')
contagem = 3
while contagem <= N:
    t3 = t1 + t2
    print(f'{t3}, ', end='')
    t1 = t2
    t2 = t3
    contagem += 1
print('FIM')