dados = list()

dados.append('Pedro') # Pedro no index 0 da lista Dados
dados.append(25) # 25 no index 1 da lista Dados

# agora, para adicionar essa lista a outra lista chamada "Pessoas", fazemos assim:
pessoas = list()
pessoas.append(dados[:]) #Cópia dos itens dos dados na lista de "pessoas"
print(pessoas)

# Agora, para criar uma lista dentro de uma lista:

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]] #Lista com 3 listas.
            #índice 0       índice 1       índice 2

print(pessoas[0][0]) #Pessoas[0] = ['Pedro', 25] # Pessoas [0] [0] = 'Pedro'
# Primeiro número se refere a qual lista dentro da lista queremos e o segundo número se refere a qual item dentro dessa
# lista queremos.

print(pessoas[1][1]) # O resultado vai ser 19.

print(pessoas[2][0]) # O resultado vai João.

print(pessoas [1]) # O resultado vai ser ['Pedro', 25]

print('-' * 30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera: # Aqui, cada p é igual a uma das listas.
    print(p)
    print(p[0]) #Assim, apenas os nomes irão aparecer.
    print(p[1]) #Assim, apenas os números irão aparecer
    print(f'{p[0]} tem {p[1]} anos de idade') #Fulano tem tantos anos de idade

print('-' * 30)

