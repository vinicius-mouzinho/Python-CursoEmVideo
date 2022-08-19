# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = dict()
jogadores = list()
totalgols = 0
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    jogador['gols'] = list()
    numPARTIDAS = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(1, numPARTIDAS + 1):
        gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}? '))
        jogador['gols'].append(gols)
        totalgols += gols
        jogador['total'] = totalgols
    jogadores.append(jogador.copy())
    while True:
        continuar = input('Deseja continuar? [S/N]: ').upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Apenas digite "S" se deseja continuar ou "N" se deseja parar.')
    if continuar == 'N':
        break

print('-=' * 30)
print(f'{"cod"}   {"nome":>4}    {"total":>10}')
print('-' * 60)
for c in range(0, len(jogadores)):
    print(f'{c}   {(jogadores[c]["nome"]):>4}  {(jogadores[c]["total"]):>10}')
print('-' * 60)
while True:
    selecao = int(input('Mostrar dados de qual jogador? (999 interrompe o programa): '))
    if selecao == 999:
        print('FIM.')
        break
    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[selecao]["nome"]}: ')
    for c in range(0, len(jogadores[selecao]["gols"])):
        print(f'No jogo {c + 1} fez {jogadores[selecao]["gols"][c]} gols.')








