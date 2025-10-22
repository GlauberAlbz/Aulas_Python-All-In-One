from os import system as sys

lista = dict() # Cria um dicionario vazio

lista = {'nome': 'Pedro', 'idade': 25}


sys('cls')

# Adicionando, Alterando e removendo itens
'''
print(lista['nome'])
print(lista['idade'])

print(f'{lista['nome']} sua idade é {lista['idade']} anos.')

lista['sexo'] = 'M'
print(lista)

del lista['idade']

print(lista)

listafilmes = dict()
'''
'''
listafilmes = {
    'nome': "Shin Godzilla",
    'ano': 2016,
    'diretor': 'Hideaki Anno'
}

print(listafilmes) # Imprime o dicionario completo

print(listafilmes.values()) # Imprime apenas os valores do dicionario, sem os campos

print(listafilmes.keys()) # Imprime apenas os campos do dicionario, sem os valores

print(listafilmes.items()) # Imprime o dicionario completo e separado

for k, v in listafilmes.items():
    print(f'O {k} é {v}')
'''
'''
pessoas = {'nome': 'Asdrubal', 'idade': 19, 'sexo': 'F'}

print(pessoas['nome'])

print(f'{pessoas['nome']} tem {pessoas['idade']} anos')

del pessoas['sexo']

pessoas['nome'] = 'Leandro'

for k,v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso'] = 95
print(pessoas)
'''

brasil = []
estado = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil.append(estado)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])

print(brasil[0]['uf'])