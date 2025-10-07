'''
    Autores: Glauber Almeida B. - Luis Henrique N. C. Pozenato
    Turma: 2ºA DS               Data: 18/09/2025

    Exercício 04
    - Faça um programa que pergunte qual tabuada o cliente quer e imprima.
'''

import os 

os.system('cls')

print('Seja Bem vindo Ao Programa da Tabuada!')

print(5*'|')
print(5*'↓')

num = int(input('Qual número deseja multiplicar?: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
print('\nObrigado por Utilizar esse programa!')
