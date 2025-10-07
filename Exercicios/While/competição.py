'''
    Autor: Glauber Almeida de Brito
    Turma: 2ºA DS               Data: 25/09/2025

    Atividade Competitiva - Glauber X Gustavo dos Santos
    - Faça um programa que leia o sexo de uma pessoa, 
      mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
      peça a digitação novamente até ter um valor correto
'''

# Importando bibliotecas necessárias
from colorama import init, Fore, Back, Style   # Para colorir textos no terminal
import os                                      # Para limpar a tela (cls)
import time                                    # Para adicionar delays (pausas)

init()               # Inicializa o colorama
os.system('cls')     # Limpa a tela logo no início do programa

# Tela inicial (título do programa)
print(Fore.CYAN + "======================================================")
print(Fore.CYAN + "||                                                  ||")
print(Fore.CYAN + "||    " + Fore.YELLOW + "BEM-VINDO AO PROGRAMA VERIFICADOR DE SEXO" + Fore.CYAN + "     ||")
print(Fore.CYAN + "||                                                  ||")
print(Fore.CYAN + "======================================================")
print(Style.RESET_ALL)
time.sleep(1)   # Pausa de 1 segundo

# Explicação inicial para o usuário
print(Fore.GREEN + "Este programa irá pedir para você inserir seu sexo." + Style.RESET_ALL)
time.sleep(1)
input(Fore.YELLOW + "Pressione ENTER para continuar..." + Style.RESET_ALL)

os.system('cls')   # Limpa a tela novamente

# Entrada de dados (usuário digita M ou F)
sexo = str(input("Qual o seu sexo? (" + Fore.BLUE + "M" + Style.RESET_ALL + "/" + Fore.MAGENTA + "F" + Style.RESET_ALL + ") ")).upper().strip()

os.system('cls')

# Estrutura de repetição: só sai quando digitar 'M' ou 'F'
while sexo != 'M' and sexo != 'F':
    print(Fore.RED + "\nErro! Por favor, digite M ou F para continuar.\n" + Style.RESET_ALL)
    sexo = str(input("Qual o seu sexo? (" + Fore.BLUE + "M" + Style.RESET_ALL + "/" + Fore.MAGENTA + "F" + Style.RESET_ALL + ") ")).upper().strip()
    os.system('cls')
    time.sleep(0.25)  # Pausa rápida para suavizar

os.system('cls')

# Mensagem de saída estilizada
frase1 = "Seu sexo é:"

# Escreve a frase letra por letra (efeito "digitando")
for letras in frase1:
    print(letras, end='', flush=True)
    time.sleep(0.1)

time.sleep(0.5)

os.system('cls')

# Efeito de "carregando..." antes de mostrar o resultado
for c in range(0, 7):
    for c in range(0, 3):
        print('.', end='', flush=True)
        time.sleep(0.15)
    os.system('cls')

# Verificação do resultado
if sexo == 'M':
    print(Fore.BLUE + "Masculino!")     # Mostra masculino em azul
else:
    print(Fore.MAGENTA + "Feminino!")    # Mostra feminino em roxo

print(Style.RESET_ALL)
time.sleep(2)   # Pausa final antes de encerrar
