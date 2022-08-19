from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou o número {v} no dado')
    sleep(1)
ranking = dict()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'O maior valor tirado no dado foi {ranking[0][1]} pelo {ranking[0][0]}!')
