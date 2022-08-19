# como criar dicionários

criardict = dict()
criardict2 = {}

# Criando um dicionário com índices "nome" e "idade:
dados = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
print(dados['idade'])

# O append não funciona no dicionário.
# Você deve usar o comando:
dados['sexo'] = 'M'

# Para remover um dado do dicionário:
del dados['idade']
print(dados)

# Criando um dicionário com os elementos título, ano e diretor:
# (esses elementos são chamados de chaves)

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'}

# Valores = Star Wars, 1977, George Lucas
print(filme.values())

# índices ou keys = Título, Ano, Diretor
print(filme.keys())

# ítens = Para mostrar tudo:
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')
    # k = índice ou key
    # v = valor ou value

# Você pode criar uma lista onde cada elemento tem um dicionário dentro.
locadora = [{'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}, {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Wheden'}]
# E você pode acessar cada valor dessa forma:
print(locadora[0]['ano'])
print(locadora[1]['titulo'])

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas[0]) = ERRO !
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.values():
    print(k)
del pessoas['sexo'] #Para deletar um item
pessoas['nome'] = 'Leandro' #agora esse é o nome
pessoas['Peso'] = 98.5 #para adicionar um item
for k, v in pessoas.items():
    print(f'{k} = {v}')

# Para criar um dicionário em uma lista

brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['UF'])
print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
