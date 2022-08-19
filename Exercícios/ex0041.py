# Crie um programa para a Confederação Nacional de Natação que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade: Até 9 anos, mirim; até 14 anos, infantil; até 19 anos, junior;
# acima, master.

print('Descubra em qual categoria de atleta você está!')
ano = int(input('Digite o ano de seu nascimento: '))

if ano >= 2013:
    print('Você está na categoria mirim!')
elif 2013 > ano > 2008:
    print('Você está na categoria infantil!')
elif 2008 > ano > 2003:
    print('Você está na categoria junior!')
elif 2003 > ano:
    print('Você está na categoria master!')