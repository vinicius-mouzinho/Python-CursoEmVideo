# Faça um programa que calcule o imc de uma pessoa e avise se ela está abaixo do peso (<18.5), no peso ideal (18.5 a 25),
# em sobrepeso(25 a 30) , obesa (30 a 40) ou em obesidade mórbida (acima de 40).

altura = float(input('Digite a sua altura, em metros: '))
peso = float(input('Digite o seu peso, em kg: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Você está abaixo do peso, com o imc de {imc:.2f}')
elif 25 > imc >= 18.5:
    print(f'Você está no peso ideal, com o imc de {imc:.2f}.')
elif 30 > imc >= 25:
    print(f'Você está em sobrepeso, com o imc de {imc:.2f}.')
elif 40 > imc >= 30:
    print(f'Você está obeso, com o imc de {imc:.2f}.')
elif imc >= 40:
    print(f'Você possui obesidade mórbida, com o imc de {imc:.2f}.')
