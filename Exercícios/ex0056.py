# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o homem mais velho e quantas mulheres têm menos de 20 anos.

mulheres_menores_de_20 = 0
media_de_idade = 0
homem_mais_velho = ''

for c in range(1, 5):
    #nome, idade e sexo
    dados = input('Digite seu nome, H ou M para indicar se você é homem ou mulher e a sua idade, separados por vírgulas: ').upper()
    div = dados.split()
    idade = int(div[2])
    media_de_idade = media_de_idade + idade/4
    print(div[1])
    if div[1] == 'M,' and idade < 20:
        mulheres_menores_de_20 = mulheres_menores_de_20 + 1
    if c == 1 and div[1] == 'H,':
        homem_mais_velho = div[1]
    else:
        if div[1] == 'H,' and


print(f'A média de idade é {media_de_idade}, há {mulheres_menores_de_20} mulheres menores de 20 e')

