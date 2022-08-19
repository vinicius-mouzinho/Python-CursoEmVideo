# Digite um número e o converterei para binário, octal ou hexadecimal.

numero = int(input('Qual número você deseja converter? '))
escolha = input('Se você deseja convertê-lo para binário, digite 1; para octal; digite 2; para hexadecimal; digite 3: ')
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if escolha == str(1):
    print(f'O seu número, na base binária, é {binario}')
elif escolha == str(2):
    print(f'O seu número, na base octal, é {octal}')
elif escolha == str(3):
    print(f'O seu número, na base hexadecimal, é {hexadecimal}')

