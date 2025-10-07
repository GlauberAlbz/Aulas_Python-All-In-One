'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    Exercício 05
    - Usuário digite um nome de me fale:
    - Quantas letras "a" tem no nome
    - Qual posição que aparece primeiro
    - Qual a posição que aparece por último
'''

nome = str(input("Qual seu nome?"))
nome_low = (nome.lower())
print(f"Seu nome possui {nome_low.count("a")} Letras A's.")
print(f"O primeiro A encontrado foi no caracter: {nome_low.find("a")+1}")
print(f"O último A encontrado foi no caracter: {nome_low.rfind("a")+1}")
