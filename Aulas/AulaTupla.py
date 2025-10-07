# -------- Utilizando o PRINT --------
from os import system
system('cls')

compras = ('Arroz', 'Feijão', 'Alho', 'Ovo', 'Leite') # Cria uma tupla utilizando (), com valores armazenados

'''
print(compras) # Imprime toda a tupla com todos os seus itens

print(compras[1]) # Imprime apenas o item 1 da tupla (no caso, feijao)

print(compras[0:2]) # Imprime a tupla entre o item zero e dois (no caso arroz, feijao)

print(len(compras)) # Imprime a quantidade de itens da tupla


# -------- Utilizando o FOR --------

for c in compras: # Imprime os itens da tupla em um for
    print(c)

for c in range(0,len(compras)): # Imprime numero entre 0 e a quantidade de itens da tupla
    print(c)


for c in range(0, len(compras)): # Imprime o item da lista acompanhado do seu valor na tupla
    print(f"{compras[c]} está na posição {c+1}")

for itens in compras: # Cria uma variavel contadora ITENS e imprime ela
    print(f"Eu vou comprar {itens}")

for pos, item in enumerate(compras): # Adiciona 2 variaveis de contador, mas para isso deve-se usar o comando IN ENUMERATE
    print(f"Eu vou comprar {item} na posição {pos+1}")

# -------- Somando Tuplas --------

a = (2,5,4)
b = (5,8,1,2)
c = b + a

print(c) 

print(c.count(4)) # Conta quantos numeros 4 tem na tupla

print(c.index(4)) # Mostra qual a posição do valor 4 na tupla, caso tenha mais de um 4, ele mostrara sempre o primeiro valor

'''