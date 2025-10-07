'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 01

    - Peça pro usuário digitar o nome dele
    - Mostre o nome com todas as letras maiúsculas
    - Mostre o nome com todas as letras minúsculas
    - Quantas letras tem o nome dele
    - Quantas letras tem o primeiro nome
'''

nome = str(input("Digite o seu nome: "))

print(50*"-","\n")

print(f"Nome em maiúculo é {nome.upper()}")

print(f"Nome em minúsculo é {nome.lower()}")

print(f"O nome tem {len("".join(nome.split()))} letras")

print(f"O primeiro nome tem {len(nome.split()[0])} letras","\n")

print(50*"-")
