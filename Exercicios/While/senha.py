'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 23/09/2025
'''


import os 
import time 

os.system('cls')

RED = "\033[0;31m"
GREEN = "\033[0;32m" 
RESET = "\033[0m"

print(50*'=')
print("Seja bem vindo a tela de inicialização do sistema!")
print(50*'=')
senha = str(input("Por favor, digite a sua senha: ")).strip()

os.system('cls')
while senha != "1324":
    print(f'{RED}Senha incorreta!{RESET}')
    senha = str(input("Tente novamente: ")).strip()
    os.system('cls')
    time.sleep(0.25)

os.system('cls')
print(f"{GREEN}Senha correta!{RESET}")
time.sleep(0.5)
print("Iniciando o sistema em:")
for c in range(5,0, -1):
    print(c)
    time.sleep(1)

os.system('cls')
for c in range(0, 5):
    for c in range(0, 3):
        print('.', end='', flush=True)
        time.sleep(0.15)
    os.system('cls')

os.system('cls')
print('Sistema iniciado.\n')
input('Pressione ENTER para entrar... ')
os.system('cls')