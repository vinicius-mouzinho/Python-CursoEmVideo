# Criando funções

def título(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre {a} e {b} é {s}')

# Para que o usuário possa colocar quantos paramêtros quiser:


def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')
    # aqui, os valores serão colocados em uma tupla.


# Uma função pode receber uma lista e trabalhar em cima dela:
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1
    print(list)


def soma2(* valores):
    soma2 = 0
    for num in valores:
        soma2 += num
    print(f'Somando os valores {valores} temos a soma {soma2}')


# Programa principal
título('     CURSO EM VÍDEO     ')
título('     APRENDA PYTHON     ')
soma(4, 5)
soma(3, 7)
soma(a=4, b=5)
contador(2, 1, 8)
contador(3, 4, 5, 6)
contador(3, 6)
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
soma2(3, 4, 7)
soma2(5, 6)
soma2(7, 8, 15, 23)


