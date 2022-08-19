# Usando while, faça um algoritmo que, lendo a razão e o termo inicial, mostre os 10 primeiros termos de uma P.A.

print('*=' * 6, end='')
print('CALCULADOR DE P.A.', end='')
print('*=' * 6)
ti = int(input('Digite o termo inicial da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
contagem = 1


print('Os 10 primeiros termos dessa P.A. são: ', end='')
while contagem < 11:
    print(f'{ti}, ', end='')
    ti = ti + razao
    contagem += 1
print('FIM')






