'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 04/09/2025

    Exercício 02
    - Crie um programa em que o usuário digite um número e fale se ele é par ou impar.

'''
import os

os.system('cls')

num = int(input("Digite um número: "))

if num % 2 == 1:
    print("O número é impar.")
else:
    print("Número é par.")