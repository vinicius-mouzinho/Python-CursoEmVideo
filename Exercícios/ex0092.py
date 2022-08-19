# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
from time import sleep

dict = {'nome': '',
        'nascimento': '',
        'ctps': '',
        'anocontrat': '',
        'salário': ''}

nome = input('Nome: ')
dict['nome'] = nome
nascimento = int(input('Ano de Nascimento: '))
dict['nascimento'] = nascimento
ctps = int(input('Carteira de trabalho (0 = não tem): '))
dict['ctps'] = ctps
if ctps == 0:
    print('-=' * 10)
    del dict['anocontrat']
    del dict['salário']
    for k, v in dict.items():
        print(f'{k} é {v}')
else:
    anocontrat = int(input('Em que ano você foi contratado? '))
    dict['anocontrat'] = anocontrat
    salário = float(input('Qual é o seu salário? R$'))
    dict['salário'] = salário
    print('-=' * 10)
    sleep(1)
    print('Calculando...')
    sleep(1)
    print('-=' * 10)
    sleep(1)
    anostrab = 2022 - anocontrat
    aposentadoria = 35 - anostrab
    dict['aposentadoria'] = aposentadoria
    for k, v in dict.items():
        print(f'{k} tem o valor {v}')
        sleep(1)
