'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 04/09/2025

    Exercício 06
    - Faça um programa que pegue a medida de 3 retas e fale se essas retas formam um triângulo.

'''

import os

os.system('cls')

reta1 = float(input("Digite o valor da reta 1: "))
reta2 = float(input("Digite o valor da reta 2: "))
reta3 = float(input("Digite o valor da reta 3: "))

if reta1 + reta2 > reta3:
    if reta2 + reta3 > reta1:
        if reta3 + reta2 > reta1:
            print("É possível montar um triângulo")
        else:
            print("Não é possível montar um triângulo")
    else:
        print("Não é possível montar um triângulo")
else:
    print("Não é possível montar um triângulo")