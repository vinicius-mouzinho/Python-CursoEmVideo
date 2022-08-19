# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou.
# O programa deve ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', num_gols=0):
    jogador = input('Nome do jogador: ')
    if jogador.strip() == '':
        jogador = '<desconhecido>'
    num_gols = input('Número de gols no campeonato: ')
    if num_gols.isnumeric():
        num_gols = int(num_gols)
    else:
        num_gols = 0
    print(f'O jogador {jogador} fez {num_gols} gol(s) no campeonato.')


ficha()

