'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 18/09/2025

    Exercício 05
    - Desenvolva um programa que leia 6 números interios e mostre a soma apenas daqueles que forem pares.
      Se o valor digitado for impar, desconsidere-o.
'''

import os

os.system('cls')

soma = 0

for c in range(6):  
    num = int(input(f"Defina o valor do número {c+1}: "))
    if num % 2 == 0:  
        soma += num
    else:
        print(f'O número {num} é impar, logo desconsideraremos esse valor da soma.')
print('\n')
print(f'O resultado da conta apenas somando os pares deu: {soma}!\n')
print('Obrigado por usar este programa!')
