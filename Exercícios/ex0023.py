#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

n = (input('Informe um número de 0 a 9999: '))
s = n.split()
if len(n) > 4:
    print('Erro! Apenas digite números de 0 a 9999.')
elif len(n) == 1:
    print(f'unidade: {s[0][0]}')
elif len(n) == 2:
    print(f'unidade: {s[0][1]}')
    print(f'dezena: {s[0][0]}')
elif len(n) == 3:
    print(f'unidade: {s[0][2]}')
    print(f'dezena: {s[0][1]}')
    print(f'centena: {s[0][0]}')
elif len(n) == 4:
    print(f'unidade: {s[0][3]}')
    print(f'dezena: {s[0][2]}')
    print(f'centena: {s[0][1]}')
    print(f'milhar: {s[0][0]}')


