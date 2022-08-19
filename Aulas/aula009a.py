frase = '   Curso em Vídeo Python   '

#Para contar quantas vezes tem "o"
print(frase.count('o'))

#Coloca a frase em maiúsculo e depois conta quantos O tem
print(frase.upper().count('O'))

#Tamanho da frase
print(len(frase))

#Tira os espaços e depois conta de novo o tamanho da frase
print(len(frase.strip()))

#Troca, na hora de printar, a palavra Python por Android
print(frase.replace('Python', 'Android'))

#Entretanto, a string é imutável, então, quando printamos novamente,
#volta a ser Python:
print(frase)

#Conferir se a palavra curso está na frase
print('Curso' in frase)

#Posição do início da palavra Curso na frase
print(frase.find('Curso'))

#Frase splitada, ou seja, criar uma lista com as palavras da frase
print(frase.split())

#Printar uma palavra da frase splitada, a partir de sua posição:
dividido = frase.split()
print(dividido[0])

#Printar uma letra da segunda palavra da frase splitada
print(dividido[2][3])

