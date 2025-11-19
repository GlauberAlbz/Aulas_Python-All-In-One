from os import system 

def linha():
    print("=" * 50)

linha()
print("Sistema alunos")
linha()
print("Cadastro alunos")
linha()

# Parametros
system('cls')
def titulo(msg):
    print(50* "=")
    print(msg)
    print(50* "=")

titulo("sistema de alunos")

system('cls')
'''
def soma(a, b):
    print(f"A = {a} e B = {b}")
    soma = a+b
    print(f"A soma A + B = {soma}")

soma(40, 90)

valor1 = int(input("Qual o valor de a?"))
valor2 = int(input("qual o valor de b?"))

soma(valor1, valor2)
'''

# Empacotadores
'''
def contador (* num):
    soma = 0
    for c in range(len(num)):
        soma += num[c]
    print(soma)
contador(1,3,5)
'''

''' forma 1 de fazer
num1 = int(input("Insira o valor de a: "))
num2 = int(input("Insira o valor de b: "))
num3 = int(input("Insira o valor de c: "))

def soma(a, b ,c):
    s = a+b+c
    print()
    print(s)

soma(num1, num2, num3)
'''

''' forma 2 de fazer
numeros = list()

for c in range(0,3):
    numeros.append(int(input(f'Digite o {c+1}º valor: ')))

def soma(num):
    soma = 0
    for c in range(0,3):
        soma += num[c]
    print(f"A soma dos valores é: {soma}")

soma(numeros)

'''

# Listas em funções
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7,2,5,0,4]

dobra(valores)
print(valores)

def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f"A soma vale {s}")

somar(3,4)
'''

# Funções globais
'''
# Escopo Global
def teste():
    print(f"Na função teste n vale {n}")

n = 2

print(f"No programa N vale {n}")
teste()
'''

# Escopo Local
'''
def teste():
    n = 2
    print(f"Na função teste n vale {n}")

teste()
# print(f"No programa N vale {n}") Não funciona
'''
'''
def teste():
    x = 3
    print(f"Na função teste n vale {n}")
    print(f"Na função teste x vale {x}")

n = 2
print(f"No programa N vale {n}")
teste()
'''

def teste(b):
    a = 2
    b = b + 3
    print(f"Na função teste a vale {a}")
    print(f"Na função teste b vale {b}")

a = 5
teste(a)
