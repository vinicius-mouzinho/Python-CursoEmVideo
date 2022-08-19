# Tratamento de erros e exceções

try:  # Pede para que o computador tente fazer uma ação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

# except Exception as erro:
    # print(f'Problema encontrado foi: {erro.__class__}') # Serve para você identificar qual a classe do erro.

except (ValueError, TypeError):
    print('ERRO! Tivemos um problema com os tipos de dados apresentados.')
except ZeroDivisionError:
    print('ERRO! Não é possível fazer uma divisão por zero')
else:  # Diz ao computador o que fazer caso o código dê certo!
    print(f'O valor da divisão é {r:1f}')
finally:  # O que vai acontecer, independente do erro ou do acerto.
    print('Volte sempre, muito obrigado!')
    quit()
