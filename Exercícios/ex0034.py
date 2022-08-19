# Faça um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1250.0, calcule um aumento de 10%.
# Para valores inferiores ou iguais, calcule um aumento de 15%.

n = int(input('Qual é o seu salário, em reais? '))
if n > 1250:
    print(f'O seu novo salário é de {n + n * 0.1}')
if n <= 1250:   
    print(f'O seu novo salário é de {n + n * 0.15}')