# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.

galera = list()
pessoa = dict()

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo[M/F]: ').upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Apenas digite "M" para masculino ou "F" para feminino.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = input('Deseja continuar? [S/N]: ').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Apenas digite "S" para sim ou "N" para não.')
    if resp == 'N':
        break
print('-=' * 30)
print(galera)
print('-=' * 30)
print('ANÁLISE: ')
print(f'Ao total, foram cadastradas {len(galera)} pessoas.')
media = 0
for c in range(0, len(galera)):
    media += (galera[c]['idade']) / len(galera)
print(f'A média de idade entre as pessoas é de {media}.')
mulheres = list()
for p in range(0, len(galera)):
    if galera[p]['sexo'] == 'F':
        mulheres.append(galera[p]['nome'])
print(f'Lista de mulheres: {mulheres}')
acimamedia = list()
for p in range(0, len(galera)):
    if galera[p]['idade'] > media:
        acimamedia.append(galera[p]['nome'])
print(f'As pessoas com idade acima da média de idade são: {acimamedia}')



