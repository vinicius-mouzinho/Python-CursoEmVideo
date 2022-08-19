# Faça um programa que sorteie a ordem de apresentação do trabalho de quatro alunos.

import random

'''
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem de apresentação será: ')
print(alunos)
'''

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
ordem = random.sample(alunos, k=2)
print('A ordem dos alunos será:')
print(ordem)
