from Exercícios.ex0108 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Com 10% de aumento, o preço torna-se {moeda. moeda(moeda.aumentar(p, 10))}')
print(f'Com 20% de desconto, o preço torna-se {moeda. moeda(moeda.diminuir(p, 20))}')
print(f'{moeda.moeda(p)}')
