# Você pode digitar help() no console do python para obter ajuda em funções internas.

# Você tb pode fazer isso assim:
help(print)

print('----')

# Ou assim para imprimir o doc:
print(input.__doc__)


# Para fazer uma docstring em uma função sua, é só colocar a informação entre três aspas duplas:
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra-a na tela.
    :param i: número de início da contagem.
    :param f: número final da contagem.
    :param p: passo da contagem.
    :return: sem retorno.
    """
    c = i
    while c <= f:
        print(f'{c }', end='')
        c += p
    print('FIM!')


help(contador)


# Parâmetros opcionais:
# o C é um parâmetro opcional. Caso ele não seja informado, o seu valor será zero, e ele não afetará a função.
def somar(a, b, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


def somartudo(* núm):
    somatotal = 0
    for valor in núm:
        somatotal += valor
    print(f'O valor da soma total dos números informados é {somatotal}')


somar(3, 5, 10)
somar(8, 7)
somartudo(3, 4, 5, 6)



