# Crie uma tupla preenchida com os 20 primeiros colocados do Brasileirão, na ordem de colocação. Depois, mostre:
# A) Apenas os cinco primeiros colocados; B) Apenas os 4 últimos colocados; C) Times em ordem alfabética;
# D) Em que posição está o Botafogo.

colocacao = ('Palmeiras', 'Corinthians', 'São Paulo', 'Internacional', 'Athletico-PR', 'Atletico-MG', 'Coritiba',
             'Fluminense', 'América-MG', 'Avaí', 'Santos', 'Bragantino', 'Ceará', 'Goiás', 'Atlético-GO', 'Flamengo',
             'Botafogo', 'Cuiabá', 'Juventude', 'Fortaleza')

print('Informações sobre a tabela do Brasileirão!')
print(f'Os cinco primeiro times são {colocacao[0:5]}.')
print(f'Os quatro últimos colocados são {colocacao[16:21]}')
print(f'Os times em ordem alfabética: {sorted(colocacao)}')
print(f'O Botafogo está na posição {colocacao.index("Botafogo") + 1}')



