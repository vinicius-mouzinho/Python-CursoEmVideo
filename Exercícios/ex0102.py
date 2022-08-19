# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
        -> Calcula o fatorial de um número.
    :param num: O número a ter seu fatorial calculado
    :param show: (opcional) Mostrar ou não o processo de cálculo do fatorial.
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for n in range(num, 1, -1):
        f *= n
    if show:
        print(f'Processo de cálculo do fatorial de {num}: ')
        for n in range(num, 1, -1):
            print(f'{n} *', end=' ')
            n -= 1
        print('1 =', end=' ')
        print(f'{f}')
    else:
        print(f'O resultado do fatorial de {num} é {f}')
    return f


print(fatorial(6, True))

