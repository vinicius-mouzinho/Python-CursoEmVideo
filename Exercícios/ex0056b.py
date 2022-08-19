# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o homem mais velho e quantas mulheres têm menos de 20 anos.

media_de_idade = 0
num_mulheres_menores_de_20 = 0
idade_homem_mais_velho = 0

for d in range(1, 5):
    print(f'------PESSOA NÚMERO {d}------')
    nome = input('Nome: ').strip()
    idade = int(input('idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    media_de_idade += idade/4
    if sexo in 'Ff' and idade < 20:
        num_mulheres_menores_de_20 += 1
    if d == 1 and sexo in 'Mm':
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

print(f'A média de idade é de {media_de_idade}')
print(f'O homem mais velho se chama {nome_homem_mais_velho} e possui {idade_homem_mais_velho} anos.')
print(f'Há {num_mulheres_menores_de_20} mulheres menores de 20 anos.')



