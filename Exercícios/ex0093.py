#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()

nome = input('Nome do jogador: ')
jogador['nome'] = nome

jogador['gols'] = list()
totalgols = 0
numpartidas = int(input(f'Quantas partidas {nome} jogou? '))
for c in range(1, numpartidas + 1):
    gols = int(input(f'Quantos gols {nome} fez na partida {c}? '))
    jogador['gols'].append(gols)
    totalgols += gols
    jogador['total'] = totalgols

print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {nome} jogou {numpartidas} partidas.')
for c in range(0, numpartidas):
    print(f'    => Na partida {c}, fez {jogador["gols"][c]} gols.')





