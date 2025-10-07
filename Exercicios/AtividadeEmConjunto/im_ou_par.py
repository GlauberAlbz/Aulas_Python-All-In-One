'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P. - Anna Caroline - Maycon Kaio S.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 02 - IF - elif
    - Faça um jogo de Impar ou Par
'''

import os
import random as rd

os.system('cls')

num_robo = rd.randint(0,5)

time = int(input("Qual o seu time? (1 - impar | 2 - par): "))
num_usuario = int(input("Escolha um número entre 0 e 5: "))
vencedor = int()

soma = num_usuario + num_robo
os.system('cls')

print(50*("="))

if time == 1:
    print("Jogador escolheu o time ímpar.")
else:
    print("Jogador escolheu o time par.")

print(f"O robô escolheu o número {num_robo}")
print(f"O usuário escolheu o número {num_usuario}")
print(f"O resultado foi {soma}")

if vencedor == 1:
    print("Portando, o resultado é ímpar.")
else:
    print("Portanto, o resultado é par.")

if soma % 2 == 1:
    vencedor = 1
else:
    vencedor = 2

if vencedor == 1:
    if time ==1:
        print("O vencedor é o Jogador!")
    else:
        print("O vencedor é o robo!")
else:
    if time == 2:
        print("O vencedor é o Jogador!")
    else:
        print("O vencedor é o robo!")


print(50*("="))