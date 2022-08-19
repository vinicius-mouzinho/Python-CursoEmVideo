# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar;
# Se é a hora de se alistar;
# Se já passou do tempo de alistamento.

print('Descubra se você já deve se alistar!')
ano = int(input('Digite o ano de seu nascimento: '))

if 2004 > ano:
    print('Já passou da hora de você se alistar!')
elif 2004 == ano:
    print('Estamos no ano do seu alistamento!')
else:
    print('Você ainda não precisa se alistar.')