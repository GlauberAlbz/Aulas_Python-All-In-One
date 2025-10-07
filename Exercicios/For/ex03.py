'''

    Autores: Glauber Almeida B. - Luis Henrique N. C. Pozenato

    Turma: 2ºA DS               Data: 21/09/2025



    Exercício 03

    - Faça um programa que calcula a soma entre todos os números que são múltiplos de Três e que se encontrem no intervalo de 1 até 500.


'''

import os
import time

os.system('cls')

soma = 0

print('Seja Bem vindo! Iremos calcular a soma entre todos os números que são múltiplos de Três e que se encontrem no intervalo de 1 até 500\n')
for c in range(3, 0, -1):
    print(c)
    time.sleep(1)

for c in range(3, 501, 3):
    soma += c
    print(soma)
    time.sleep(0.05)
    os.system('cls')
print(f'O Resultado da soma foi: {soma}!')
print('Obrigado por utilizar nosso Programa!')
