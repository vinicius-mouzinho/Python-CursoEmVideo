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



