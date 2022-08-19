# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.

listatemp = list()
lista = list()

while True:
    nome = input('Diga o nome do aluno: ')
    n1 = float(input('Diga a primeira nota do aluno: '))
    n2 = float(input('Diga a segunda nota do aluno: '))
    listatemp.append(nome)
    listatemp.append(n1)
    listatemp.append(n2)
    n3 = (n1 + n2) / 2
    listatemp.append(n3)
    lista.append(listatemp[:])
    listatemp.clear()
    continuar = input('Deseja continuar? [S/N]: ')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":>4}    {"NOME":<10}    {"MÉDIA":>8}')
print('--------------------')
for i, l in enumerate(lista):
    print(f'{i:>4}    {l[0]:>10}    [{(l[3]):>8.1f}]')
print('--------------------')
vernota = int(input('Mostrar notas do aluno com qual "No."? (999 interrompe): '))
while vernota != 999:
    print(f'Notas do aluno {lista[vernota][0]} são {lista[vernota][1]} e {lista[vernota][2]}')
    vernota = int(input('Mostrar notas do aluno com qual "No."? (999 interrompe): '))