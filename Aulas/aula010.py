'''nome = input('Qual é o seu nome? ')
if nome == 'Vinícius':
    print('Que nome lindo você tem!')
else: print('Seu nome é tão normal...')
print(f'Bom dia, {nome}!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1+n2)/2

if m == 10:
    print(f"Parabéns, você é um aluno nota 10!")
elif 10 > m > 7:
    print(f"Parabéns! Você passou com média {m:.2f}!")
elif 7 > m:
    print(f'Você está reprovado com média {m:.2f}, estude mais!')
elif m > 10:
    print('Digite apenas notas de 0 a 10.')