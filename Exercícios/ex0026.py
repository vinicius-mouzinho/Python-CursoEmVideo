# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra ''A''
# Em que posição aparece pela primeira vez
# Em que posição ela aparece pela ultima vez

frase = input('Digite uma frase: ').strip()
print(f'A letra "A" aparece {frase.upper().count("A")} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {frase.upper().find("A")}')
