from Exercícios.ex0107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Com 10% de aumento, o preço torna-se {moeda.aumentar(p, 10)}')
print(f'Com 20% de desconto, o preço torna-se {moeda.diminuir(p, 20)}')
