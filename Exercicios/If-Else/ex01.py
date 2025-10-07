'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 04/09/2025

    Exercício 01
    - Crie um programa que o computador pense em um número e o usuário tente adivinhar.

'''

import random
import os

os.system('cls')

tentativa = int()
numsecret = random.randint(1, 1000)
print('Seja Bem vindo ao Jogo da adivinhação!\n\n')

while numsecret != tentativa:
    tentativa = int(input('Tente Acertar o Numero secreto: '))
    if tentativa < numsecret:
        print("O Valor é mais alto!\n")
    elif tentativa > 1000:
        print('Você está saindo dos limites, tente chutar mais baixo.')
    elif tentativa > numsecret:
        print('Chute Mais Baixo!\n')
                
print('Você Acertou!!! Parabéns!')