# Sistema de cores

# Style -> 0 = normal; 1 = negrito; 4 = sublinhado; 7 = inversão das cores
# Text -> 30 = branco; 31 = vermelho; 32 = verde; 33 = amarelo; 34 = azul; 35 = roxo; 36 = esmeralda; 37 = cinza
# Back (fundo) -> mesmas sequência de cima, só trocar o 3 por 4 = 40, 41, 42, 43....
# iniciar cor = \033[0:30:40m
# terminar cor = \033[m

'''a = 3
b = 5
print(f'Os valores são \033[1;31m{a}\033[m e \033[32m{b}\033[m')'''

nome = 'Vinicius'
print(f'Olá! Muito prazer em te conhecer, \033[31m{nome}\033[m!')