# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

números = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar!')
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
print('-' * 30)
print(f'Você digitou os valores {números}')
print(f'A ordem crescente desses números é {sorted(números)}')

