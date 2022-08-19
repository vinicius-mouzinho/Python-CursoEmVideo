#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

nome = input('Informe o nome da cidade: ')

#Para retirar espaços desnecessários/letras maiusc e minusc e a contagem ser correta:
n = nome.upper().strip

if nome.find('Santo') == 0:
    print('A palavra começa com "Santo".')
else:
    print('A palavra não começa com "Santo".')




