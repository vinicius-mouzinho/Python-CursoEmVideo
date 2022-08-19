# Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante ao input, mas fazendo a
# validação para aceitar apenas um valor numérico.

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
