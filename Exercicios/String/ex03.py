'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 03
    - Crie um programa que leia o nome de uma cidade e ele fale se ela começa com a palavra santo
   
'''

cidade = str(input("Digite o nome de uma cidade: "))

print("Santo" in cidade.split()[0])