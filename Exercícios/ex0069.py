# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre: A) Quantas pessoas tem mais de 18 anos; B) Quantos homens foram
# cadastrados; C) Quantas mulheres tem menos de 20 anos.

maiores = 0
homens = 0
mulheres_menores = 0
idade = int(input('Digite sua idade: '))
sexo = input('Qual é o seu sexo biológico? [M/F]: ')

while True:
    while sexo not in 'FfMm':
        sexo = input('Qual é o seu sexo biológico? [M/F]: ')
    if idade >= 18:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres_menores += 1
    print(('-' * 40))
    print(f'Registrada pessoa do sexo {sexo} com {idade} anos com sucesso!')
    print('-' * 40)
    continuar = input('Deseja continuar? [S/N]: ')
    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [S/N]: ')
    if continuar in 'Ss':
        print('-' * 40)
        idade = int(input('Digite sua idade: '))
        sexo = input('Qual é o seu sexo biológico? [M/F]: ')
    if continuar in 'Nn':
        print('-' * 40)
        break

print(f'Foram cadastrados {maiores} pessoas maiores de idade')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulheres_menores} mulheres menores de 20 anos de idade')
