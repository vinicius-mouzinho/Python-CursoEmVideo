núm = [[], []]

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

print(f'A lista ímpar ordenada é {sorted(núm[1])}')
print(f'A lista par ordenada é {sorted(núm[0])}')