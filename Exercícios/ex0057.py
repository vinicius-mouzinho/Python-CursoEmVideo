# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.


sexo = input('Qual é o seu sexo biológico? [M/F]: ').strip().upper()[0]

while sexo not in 'FfMm':
    sexo = str(input('Você digitou um valor errado! Digite apenas M ou F: '))

if sexo in 'Mm':
    print(f'Seu sexo biológico é masculino.')

if sexo in 'Ff':
    print(f'Seu sexo biológico é feminino.')
