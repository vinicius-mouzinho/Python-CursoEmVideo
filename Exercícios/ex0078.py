# Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, pra cada
# palavra, quais são as suas vogais.

lista = ('Vinicius', 'Gabryel', 'Dhiego', 'Alice', 'Luana', 'Alanis', 'Pedro')

for palavra in lista:
    print(f'\n"{palavra}" tem as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')