def resumo(preço, aumento, redução):
    frase = 'RESUMO DO VALOR'
    print('-' * len(frase))
    print(frase)
    print('-' * len(frase))
    print(f'Preço analisado: R${preço:.2f}'.replace('.', ','))
    print(f'Dobro do preço R${preço * 2:.2f}'.replace('.', ','))
    print(f'Metade do preço R${preço / 2:.2f}'.replace('.', ','))
    print(f'{aumento}% de aumento: R${preço + (preço * aumento / 100):.2f}'.replace('.', ','))
    print(f'{redução}% de redução: R${preço - (preço * redução / 100):.2f}'.replace('.', ','))
