'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 06
    - Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e último nome separadamente
    - Ex. Lindolfo Batista Franca Junior
    - Primeiro nome = Lindolfo
    - Segundo nome = Junior
'''

nome = str(input("Digite o seu nome completo: "))

print(f"{nome.split()[0]}")
print(f"{nome.split()[1]}")