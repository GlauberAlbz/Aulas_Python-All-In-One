'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes Calazans P.
    Turma: 2ºA DS               Data: 16/10/2025

    Fazer um programa com 3 etapas:
    1. Login e Cadastro
    2. Programa(Sorteado)
    3. Encerramento

    Programa:
        Fazer um programa que realiza uma pesquisa em relação aos Sistemas Operacionais:
        1. Windows - 2. Linux - 3. MacOS - 4. Unix - 5. Outros
        O programa deve pegar as respostas dos usuários, deverá parar quando digitar 0.
        Deve ser exibido dessa maneira:
        - Windows 100 votos - 50%
        - Linux 50 votos - 30%
        - MacOS 30 votos - 15%
        - Unix 20 votos - 5%
    
'''

from os import system as sys
from time import sleep
from colorama import Fore, Back, Style, init

vermelho = Fore.RED
verde = Fore.GREEN
azul = Fore.BLUE
amarelo = Fore.YELLOW
ciano = Fore.CYAN
magenta = Fore.MAGENTA
branco = Fore.WHITE
preto = Fore.BLACK
reset = Style.RESET_ALL
negrito = Style.BRIGHT

# Glauber - Programa
loop_programa = True
loop_resultado = False
participante = 1
total_respostas = 0
sistemas = [['Windows', 0], ['Linux', 0], ['MacOS', 0], ['Unix', 0], ['Outros', 0]]
resposta = str()

while loop_programa == True:
    sys('cls')
    print(ciano + negrito + '╔' + '═' * 73 + '╗')
    print('║' + amarelo + f'Participante {participante}'.center(73) + ciano + '║')
    print('╠' + '═' * 73 + '╣')
    print('║' + branco + 'Qual o melhor Sistema Operacional em sua opinião?'.center(73) + ciano + '║')
    print('║' + verde + '1 - Windows'.center(73) + ciano + '║')
    print('║' + verde+ '2 - Linux'.center(73) + ciano + '║')
    print('║' + verde + '3 - MacOS'.center(73) + ciano + '║')
    print('║' + verde + '4 - Unix'.center(73) + ciano + '║')
    print('║' + verde + '5 - Outros'.center(73) + ciano + '║')
    print('║' + vermelho + '0 - Sair do programa'.center(73) + ciano + '║')
    print('╚' + '═' * 73 + '╝' + reset)
    resposta = input(amarelo + 'Digite a sua resposta: ' + reset).strip()
    sys('cls')

    while resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4' and resposta != '5' and resposta != '0':
        sys('cls')
        print(ciano + negrito + '╔' + '═' * 73 + '╗')
        print('║' + amarelo + f'Participante {participante}'.center(73) + ciano + '║')
        print('╠' + '═' * 73 + '╣')
        print('║' + branco + 'Qual o melhor Sistema Operacional em sua opinião?'.center(73) + ciano + '║')
        print('║' + verde + '1 - Windows'.center(73) + ciano + '║')
        print('║' + verde+ '2 - Linux'.center(73) + ciano + '║')
        print('║' + verde + '3 - MacOS'.center(73) + ciano + '║')
        print('║' + verde + '4 - Unix'.center(73) + ciano + '║')
        print('║' + verde + '5 - Outros'.center(73) + ciano + '║')
        print('║' + vermelho + '0 - Sair do programa'.center(73) + ciano + '║')
        print('╚' + '═' * 73 + '╝' + reset)
        print(vermelho + f'Digito Inválido! (1, 2, 3, 4, 5, 0)' + reset)
        resposta = input(amarelo + 'Digite a sua resposta: ' + reset).strip()
        sys('cls')

    match resposta:
        case '1':
            sistemas[0][1] += 1
            participante += 1
        case '2':
            sistemas[1][1] += 1
            participante += 1
        case '3':
            sistemas[2][1] += 1
            participante += 1
        case '4':
            sistemas[3][1] += 1
            participante += 1
        case '5':
            sistemas[4][1] += 1
            participante += 1
        case '0':
            loop_resultado = True

            total_respostas = sistemas[0][1] + sistemas[1][1] + sistemas[2][1] + sistemas[3][1] + sistemas[4][1]

            if sistemas[0][1] != 0:
                sistemas[0].append(sistemas[0][1] / total_respostas * 100) # Windows
            else:
                sistemas[0].append(0)

            if sistemas[1][1] != 0:
                sistemas[1].append(sistemas[1][1] / total_respostas * 100) # Linux
            else:
                sistemas[1].append(0)

            if sistemas[2][1] != 0:
                sistemas[2].append(sistemas[2][1] / total_respostas * 100) # MacOS
            else:
                sistemas[2].append(0)

            if sistemas[3][1] != 0:
                sistemas[3].append(sistemas[3][1] / total_respostas * 100) # Unix
            else:
                sistemas[3].append(0)

            if sistemas[4][1] != 0:
                sistemas[4].append(sistemas[4][1] / total_respostas * 100) # Outros
            else:
                sistemas[4].append(0)
        

    while loop_resultado == True:

        if total_respostas == 0:
            sys('cls')
            print(ciano + negrito + '╔' + '═' * 73 + '╗')
            print('║' + vermelho + 'Não tem como fazer uma pesquisa com 0 participantes!'.center(73) + ciano + '║')
            print('║' + branco + 'Deseja tentar novamente? S/N:'.center(73) + ciano + '║')
            print(ciano + '╚' + '═' * 73 + '╝' + reset)
            sim_ou_nao = str(input(amarelo + 'Digite a sua resposta: ' + reset)).strip().upper()

            while sim_ou_nao != 'S' and sim_ou_nao != 'N':
                sys('cls')
                print(ciano + negrito + '╔' + '═' * 73 + '╗')
                print('║' + vermelho + 'Não tem como fazer uma pesquisa com 0 participantes!'.center(73) + ciano + '║')
                print('║' + branco + 'Deseja tentar novamente? S/N:'.center(73) + ciano + '║')
                print(ciano + '╚' + '═' * 73 + '╝' + reset)
                print(vermelho + 'Digito Inválido! (S ou N)' + reset)
                sim_ou_nao = str(input(amarelo + 'Digite a sua resposta: ' + reset)).strip().upper()

            if sim_ou_nao == 'S':
                loop_resultado = False
                loop_programa = True
            else:
                loop_programa = False
                loop_resultado = False
        else:
            sys('cls')
            print(ciano + negrito + '╔' + '═' * 73 + '╗')
            print('║' + amarelo + f"Total de participantes: {total_respostas}".center(73) + ciano + '║')
            print(ciano + f"╠{'═'*73}╣")
            print('║' + verde + f"Windows {sistemas[0][1]} - {sistemas[0][2]:.1f}%".center(73) + ciano + '║')
            print('║' + verde + f"Linux {sistemas[1][1]} - {sistemas[1][2]:.1f}%".center(73) + ciano + '║')
            print('║' + verde + f"MacOS {sistemas[2][1]} - {sistemas[2][2]:.1f}%".center(73) + ciano + '║')
            print('║' + verde + f"Unix {sistemas[3][1]} - {sistemas[3][2]:.1f}%".center(73) + ciano + '║')
            print('║' + verde + f"Outros {sistemas[4][1]} - {sistemas[4][2]:.1f}%".center(73) + ciano + '║')
            print('╠' + '═' * 73 + '╣')
            print('║' + verde + 'Deseja realizar uma nova pesquisa? S/N: '.center(73) + ciano + '║')
            print(ciano + '╚' + '═' * 73 + '╝' + reset)
            sim_ou_nao = str(input(amarelo + 'Digite a sua resposta: ' + reset)).strip().upper()

            while sim_ou_nao != 'S' and sim_ou_nao != 'N':
                sys('cls')
                print(ciano + negrito + '╔' + '═' * 73 + '╗')
                print('║' + amarelo + f"Total de participantes: {total_respostas}".center(73) + ciano + '║')
                print(ciano + f"╠{'═'*73}╣")
                print('║' + verde + f"Windows {sistemas[0][1]} - {sistemas[0][2]:.1f}%".center(73) + ciano + '║')
                print('║' + verde + f"Linux {sistemas[1][1]} - {sistemas[1][2]:.1f}%".center(73) + ciano + '║')
                print('║' + verde + f"MacOS {sistemas[2][1]} - {sistemas[2][2]:.1f}%".center(73) + ciano + '║')
                print('║' + verde + f"Unix {sistemas[3][1]} - {sistemas[3][2]:.1f}%".center(73) + ciano + '║')
                print('║' + verde + f"Outros {sistemas[4][1]} - {sistemas[4][2]:.1f}%".center(73) + ciano + '║')
                print('╠' + '═' * 73 + '╣')
                print('║' + verde + 'Deseja realizar uma nova pesquisa? S/N: '.center(73) + ciano + '║')
                print(ciano + '╚' + '═' * 73 + '╝' + reset)
                print(vermelho + 'Digito Inválido! (S ou N)' + reset)
                sim_ou_nao = str(input(amarelo + 'Digite a sua resposta: ' + reset)).strip().upper()

            if sim_ou_nao == 'S':
                loop_resultado = False
                loop_programa = True
                participante = 1
                total_respostas = 0
                sistemas = [['Windows', 0], ['Linux', 0], ['MacOS', 0], ['Unix', 0], ['Outros', 0]]
                resposta = str()
            else:
                loop_programa = False
                loop_resultado = False

sys('cls')
print('╔' + '═' * 73 + '╗')
print('║' + ' ' * 73 + '║')
print('║' + '💻  PROGRAMA ENCERRADO COM SUCESSO! 💻'.center(71) + '║')
print('║' + ' ' * 73 + '║')
print('╚' + '═' * 73 + '╝')



