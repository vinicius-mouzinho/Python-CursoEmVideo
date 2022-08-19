# Faça um algoritmo que crie uma P.A. onde o usuário pode selecionar quantos termos da P.A. ele deseja receber.
# O programa terminará quando ele disser que quer mostrar 0 termos.


ti = int(input('Digite o termo inicial da sua P.A.: '))
razao = int(input('Digite a razão da sua P.A.: '))
n = int(input('Quantos termos você quer ver na sua P.A? '))
contagem = 0

while contagem < n:
    print(f'{ti}, ', end='')
    ti = ti + razao
    contagem += 1
    if contagem == n:
        print('FIM')
        ti = ti - (razao * contagem)
        contagem = 0
        n = int(input('\nQuantos termos você quer ver na sua P.A.? '))
    if n == 0:
        print('FIM')







