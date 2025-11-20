from os import system
system("cls")
'''
def somar(a=0, b=0, c=0):
    soma = a+b+c
    print(f"A soma vale {soma}")

somar(3,4,7)
somar(3,4)
somar(3)
'''

'''
def somar(a=0, b=0, c=0):
    soma = a+b+c
    return soma

# r1 = somar(3,4,7)
# r2 = somar(3,4)
# r3 = somar(3)
# print(f"As somas deram {r1}, {r2}, {r3}")

print(f"As somas deram {somar(3,4,7)}, {somar(3,4)}, {somar(3)}")
'''

'''
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
'''

def parimpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número: "))

if parimpar(num):
    print("É par!")
else:
    print("É impar!")