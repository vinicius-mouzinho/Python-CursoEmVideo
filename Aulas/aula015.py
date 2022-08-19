# loop infinito

'''cont = 1
while True:
    print(cont)
    cont += 1'''

#ainda infinito

'''n = 0
while n != 999:
n = int(input('Digite um número inteiro: '))'''

#usando break

n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')