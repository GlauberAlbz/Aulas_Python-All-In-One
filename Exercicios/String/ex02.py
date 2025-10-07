'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 02
    - Faça um programa que leia um número entre 0 e 9999 e mostre:
    - Unidades
    - Dezenas
    - Centenas
    - Milhares
'''


num = int(input("Digite um numero entre 0 e 9999"))

u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10

print(u)
print(d)
print(c)
print(m)

'''
num = str(input("digite um numero de 0 a 9999 (com 4 casas): ")) #Lê o Número que o usuário inseriu
caracteres = list(num) # separa os caracteres
# Exibição
print(f"Unidade: {caracteres[3]}")
print(f"Dezena: {caracteres[2]}")
print(f"Centenas: {caracteres[1]}")
print(f"Milhares: {caracteres[0]}")
'''
