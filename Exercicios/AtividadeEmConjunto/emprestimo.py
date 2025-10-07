'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P. - Anna Caroline - Maycon Kaio S.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício Final - IF - elif
    - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
      o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
      ou então o empréstimo será negado
'''

import math
import os

os.system('cls')

print("Seja bem vindo! Aqui você poderá verificar se está apto para fazer um emprétimo bancário para a compra de uma casa. \n")

valor_casa = float(input("Qual o valor da casa que você deseja comprar? "))
salario = float(input("Qual o seu salário? "))
anos_pagamento = int(input("Em quantos anos você quer pagar a sua casa?"))

prestacao_mensal = valor_casa / (anos_pagamento*12)
porc_prest_mensal = (prestacao_mensal / salario) * 100 # Porcentagem de prestação mensal em relação ao salário

os.system('cls')

print(75*"=")
if prestacao_mensal > salario * 0.3:
    print(f"Valor da casa: R${valor_casa:.2f}")
    print(f"Salário: R${salario:.2f}")
    print(f"Anos de pagamento: {anos_pagamento}")
    print(f"Prestação mensal: R${prestacao_mensal:.2f}")
    print(f"Porcentagem da prestação mensal em relação ao salário: {porc_prest_mensal:.2f}%")
    print(75*"-")
    print("Você não está apto para fazer um empréstimo.")
    print("A prestação mensal excede o limite de 30% do seu salário")
else:
    print(f"Valor da casa: R${valor_casa:.2f}")
    print(f"Salário: R${salario:.2f}")
    print(f"Anos de pagamento: {anos_pagamento}")
    print(f"Prestação mensal: R${prestacao_mensal:.2f}")
    print(f"Porcentagem da prestação mensal em relação ao salário: {porc_prest_mensal:.2f}%")
    print(75*"-")
    print("Você está apto para fazer um empréstimo bancário!")
print(75*"=")
