def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Digite um número float válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return f


inteiro = leiaint('Digite um valor: ')
float = leiafloat('Digite um valor: ')
print(f'O valor inteiro digitado foi {inteiro} e o float foi {float}')


