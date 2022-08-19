# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando
# quantas vitórias consecutivas ele conquistou até o final do jogo.

from random import randint


print('Vamos jogar par ou ímpar!')
escolha_usuario = input('Você escolhe par ou ímpar? Digite 1 para ímpar e 2 para par: ')
escolha_pc = vitorias_usuario = vitorias_pc = 0

if escolha_usuario == '1':
    escolha_pc = '2'
if escolha_usuario == '2':
    escolha_pc = '1'

numero_usuario = int(input('Agora escolha um número: '))
numero_pc = randint(1, 10)
resultado = numero_usuario + numero_pc

while True:
    print(f'O computador escolheu {numero_pc}')
    print(f'O resultado é {numero_usuario} + {numero_pc} = {resultado}!')
    if resultado % 2 == 0 and escolha_usuario == '2' or resultado %2 != 0 and escolha_usuario == '1':
        print('Você ganhou! Vamos jogar novamente!')
        vitorias_usuario += 1
        escolha_usuario = input('Você escolhe par ou ímpar? Digite 1 para ímpar e 2 para par: ')
        numero_usuario = int(input('Agora escolha um número: '))
        numero_pc = randint(1, 10)
        resultado = numero_usuario + numero_pc
    else:
        break

print(f'Fim! Você ganhou do computador {vitorias_usuario} vezes consecutivas!')




