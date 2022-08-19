#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas;
# O nome com todas as letras minúsculas;
# Quantas letras o nome possui, sem considerar espaços;
# Quantas letras tem o primeiro nome.

nome = input("Informe seu nome completo: ")
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')
nome_sem_espacos = len(nome) - nome.count(' ')
print(f'Seu nome possui esse número de letras: {nome_sem_espacos}')
split = nome.split()
print(f'Seu primeiro nome é {split[0]} e ele possui {len(split[0])} letras')
