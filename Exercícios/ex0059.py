# Faça um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
soma = n1 + n2
multiplicacao = n1 * n2


escolha = int(input('O que você deseja fazer com esses números? [1] somar [2] multiplicar [3] descobrir o maior [4] escolher novos números [5] sair do programa: '))

while escolha != 5:
    if escolha == 1:
        print(f'A soma desses números é {soma}')
        escolha = int(input('O que você deseja fazer com esses números? [1] somar [2] multiplicar [3] descobrir o maior [4] escolher novos números [5] sair do programa: '))
    if escolha == 2:
        print(f'A multiplicação desses números é {multiplicacao}')
        escolha = int(input('O que você deseja fazer com esses números? [1] somar [2] multiplicar [3] descobrir o maior [4] escolher novos números [5] sair do programa: '))
    if escolha == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        if n2 > n1:
            print(f'O maior número é {n2}')
        if n1 == n2:
            print('Ambos os números são iguais.')
        escolha = int(input('O que você deseja fazer com esses números? [1] somar [2] multiplicar [3] descobrir o maior [4] escolher novos números [5] sair do programa: '))
    if escolha == 4:
        n1 = int(input('Informe um número: '))
        n2 = int(input('Informe outro número: '))
        escolha = int(input('O que você deseja fazer com esses números? [1] somar [2] multiplicar [3] descobrir o maior [4] escolher novos números [5] sair do programa: '))
