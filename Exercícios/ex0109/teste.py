from Exercícios.ex0109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Com 10% de aumento, o preço torna-se {moeda.aumentar(p, 10, True)}')
print(f'Com 20% de desconto, o preço torna-se {moeda.diminuir(p, 20, True)}')
