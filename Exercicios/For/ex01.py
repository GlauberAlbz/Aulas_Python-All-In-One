'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 18/09/2025

    Exercício 01
    - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
      indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

import os
import time 

os.system('cls')

print("Segue a contagem regressiva dos fogos de artifício:")

for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print("FELIZ ANO NOVO!!!🎆🎆🎆")
