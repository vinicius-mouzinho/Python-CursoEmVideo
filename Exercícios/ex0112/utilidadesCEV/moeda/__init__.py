def resumo(preço, aumento, redução):
    frase = 'RESUMO DO VALOR'
    print('-' * len(frase))
    print(frase)
    print('-' * len(frase))
    print(f'Preço analisado: R${preço:.2f}'.replace('.', ','))
    print(f'Dobro do preço: R${preço * 2:.2f}'.replace('.', ','))
    print(f'Metade do preço: R${preço / 2:.2f}'.replace('.', ','))
    print(f'{aumento}% de aumento: R${preço + (preço * aumento / 100):.2f}'.replace('.', ','))
    print(f'{redução}% de redução: R${preço - (preço * redução / 100):.2f}'.replace('.', ','))


def aumentar(preço=0, taxa=0, formatacao=False):
    res = preço + (preço * taxa / 100)
    return res if formatacao is False else moeda(res)


def diminuir(preço=0, taxa=0, formatacao=False):
    res = preço - (preço * taxa / 100)
    return res if formatacao is False else moeda(res)


def dobro(preço=0, formatacao=False):
    res = preço * 2
    return res if formatacao is False else moeda(res)


def metade(preço=0, formatacao=False):
    res = preço / 2
    return res if formatacao is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


