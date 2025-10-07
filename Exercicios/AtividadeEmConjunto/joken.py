import random as rd

import os

os.system('cls')

elementos = ["pedra", "papel", "tesoura"]
iaresposta = rd.choice(elementos)
print("1 - Pedra\n2 - Papel\n3 - Tesoura\n") 
user = int(input("Sua jogada: "))

print(f"Máquina Escolheu: {iaresposta}!")

if user == 1 and iaresposta == 'papel': 
    print('---Você Perdeu---')

elif user == 2 and iaresposta == 'tesoura': 
    print("---Você perdeu---")

elif user == 3 and iaresposta == 'pedra': 
    print("---Você perdeu---")

elif user == 1 and iaresposta == 'pedra':
    print('---EMPATE!---')

elif user == 2 and iaresposta == 'papel': 
    print('---EMPATE---!')

elif user == 3 and iaresposta == 'tesoura': 
    print('---EMPATE---!')

else: 
    print("---VOCÊ GANHOU!!!---")

print("Obrigado por jogar!")