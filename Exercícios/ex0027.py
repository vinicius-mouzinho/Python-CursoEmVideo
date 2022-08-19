# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o seu primeiro e o último nome separadamente.

nome = input('Informe o seu nome: ').strip()
split = nome.split()
print(f'O seu primeiro nome é {split[0]}, e o seu último nome é {split[-1]}')
