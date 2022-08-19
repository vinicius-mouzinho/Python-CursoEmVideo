# Aprendendo escopo de variáveis


def teste():
    global x
    n = 6
    print(f'Na função teste, x vale {x}')
    print(f'Na função teste, n vale {n}')


# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
# print(f'No programa principal, x vale {x}')
# Erro, pois a variável x foi declarada apenas na função teste. Ela possui um escopo local.
teste()
