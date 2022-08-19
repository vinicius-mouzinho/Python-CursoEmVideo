"""
Ordem de preferência

1 = ()
2 = **
3 = * / // %
4 = + -

"""

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
sm = n1 + n2
m = n1 * n2
d = n1 / n2
sb = n1 - n2
print(f'A soma vale {sm}')
print(f'A multiplicação vale {m}')
print(f'A divisão vale {d}')
print(f'A subtração vale {sb}')


