# Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dicionario = dict()
dicionario['Nome'] = input('Nome: ')
dicionario['Média'] = float(input('Média: '))
if dicionario['Média'] >= 7.0:
    dicionario['Situação'] = 'aprovado'
else:
    dicionario['Situação'] = 'reprovado'

'''print(f'Nome é igual a {dicionario["Nome"]}')
print(f'Média é igual a {dicionario["Média"]}')
print(f'A situação desse aluno é: {dicionario["Situação"]}')'''

print('-='*20)
for k, v in dicionario.items():
    print(f'{k}: {v}')