# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se a pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if ano > 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 18 > ano >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif 16 > ano:
        return f'Com {idade} anos: VOTO NEGADO'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

