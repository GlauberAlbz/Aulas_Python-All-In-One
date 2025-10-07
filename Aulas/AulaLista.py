from os import system as s; s('cls')
import random as rd

compras = ['arroz', 'feijão', 'alho', 'ovo', 'leite']

# -------------------- Alterando Itens --------------------
'''
print(compras)

compras[3] = 'frango'

print(compras)

compras[1] = 'feijoada'

print(compras)
'''
# -------------------- Incluindo Itens --------------------
'''
compras.append("café")

print(compras)

compras.insert(0,"pão")

print(compras)
'''
# -------------------- Apagando Itens --------------------
'''
compras.remove("alho")
del compras[3]
compras.pop(3)

print(compras)

if 'chocolate' in compras:
    compras.remove('chocolate')
    print('Item excluído com sucesso.')
    print(compras)
else:
    print('Não tem chocolate')
'''
# -------------------- Ordenando Listas --------------------
'''
valores = list(range(4,11))
print(valores)

numeros = [1, 3, 2, 22, 9]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)
'''
# -------------------- Praticando --------------------

val = []

val.append(5)
val.append(9)
val.append(6)
'''
print(val)

for v in val:
    print(f'{v}...', end='')

print()

for v in val:
    print(v, end=' ')

print()

for c, v in enumerate(val):
    print(f'Na posição {c+1} encontrei o valor {v}')
print('Cheguei ao final da lista')


lista_usu = list()

for cont in range(0,5):
    lista_usu.append(int(input("Digite um valor: ")))

for c, v in enumerate(lista_usu):
    print(f"Na posição {c+1} encontrei o valor {v}") 
print("Cheguei no final da lista")
'''
# -------------------- Ligação de Listas --------------------
'''
a = [2,4,5]
b = a

print(f'Lista A = {a}')
print(f'Lista B = {b}')

b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')
'''
a = [2,4,5]
b = a[:]

print(f'Lista A = {a}')
print(f'Lista B = {b}')

b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')