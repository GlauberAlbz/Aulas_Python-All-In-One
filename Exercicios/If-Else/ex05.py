'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 04/09/2025

    Exercício 05
    - Crie um programa que pegue o salário de um funcionário
    - Se ele ganhar menos que R$2000,00 - Dê um bônus de 15%
    - Se ele tiver filhos, pagar R$200,00 por filho

'''

import os

os.system('cls')

salario = float(input("Digite o seu sálario: "))
filhos = int(input("Digite quantos filhos você tem: "))
bonus_pobre = float()
bonus_filho = int()

if salario < 2000:
    reajuste_salario = float()
    bonus_pobre = salario * 0.15
    bonus_filho = filhos * 200
    reajuste_salario = salario + bonus_pobre + bonus_filho
else:
    bonus_filho = filhos * 200
    reajuste_salario = salario + bonus_filho

print("\n")
print(50*"-")
if bonus_pobre != 0:
    print(f"Você recebeu um bônus salárial de: R${bonus_pobre:.2f}. Pois seu salário é menor que R$2000,00.")

if bonus_filho != 0:
    print(f"Você recebeu um bônus salárial de: R${bonus_filho:.2f}. Pois você possui {filhos} filho(s). ")

if reajuste_salario == salario:
    print("Você não recebeu nenhum bônus salarial.")
    print(f"O seu salário é: R${salario:.2f}")
else:
    print(f"O seu salário reajustado é de R${reajuste_salario:.2f}")

print(50*"-")