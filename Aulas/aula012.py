# Condições aninhadas

nome = input('Qual é o seu nome? ')

if nome == 'Vinícius':
    print('Que nome liiiiiindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Matheus':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Alice':
    print('Que belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print(f'Tenha um bom dia, {nome}!')
