
x = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(x)}')
print(f'Só tem espaços? {x.isspace()}')
print(f'É um valor numérico? {x.isnumeric()}')
print(f'É uma palavra? {x.isalpha()}')
print(f'É alfanumérico? {x.isalnum()}')
print(f'Está com letras maiúsculas apenas? {x.isupper()}')
print(f'Está com letras minúsculas apenas? {x.islower()}')
print(f'Está capitalizada? {x.istitle()}')


