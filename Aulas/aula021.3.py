# Você pode usar o return para associar o resultado das funções a variáveis.

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(2, 3, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')


# Fazendo o cálculo do fatorial de um número e retornando-o na tela


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


# Return não funciona apenas com números:


def par(numm=0):
    if numm % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')
