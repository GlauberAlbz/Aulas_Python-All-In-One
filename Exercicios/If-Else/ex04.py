'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 04/09/2025

    Exercício 04
    - Crie um programa que o usuário digite um ano e ele responde se é ano Bissexto

'''
import os

os.system('cls')

ano = int(input("Digite um ano para descobrir se é Bissexto: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("É bissexto!")
        else:
           print("Não é bissexto!")
    else:
        print("É bissexto!")
else:
    print("Não é bissexto!")
