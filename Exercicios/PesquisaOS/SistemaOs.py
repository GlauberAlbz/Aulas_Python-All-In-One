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

# Glauber - Programa
loop_principal = True
loop_resposta = False
participante = 1
total_respostas = int()

while loop_principal == True:
    resposta = str()
    sistemas = [['Windows', 0], ['Linux', 0], ['MacOS', 0], ['Unix', 0], ['Outros', 0]]
    
    sys('cls')
    print(75*'=')
    print(f'Participante {participante}')
    print(75*'=')
    print('Qual o melhor Sistema Operacional em sua opinião?')
    print('1 - Windows')
    print('2 - Linux')
    print('3 - MacOS')
    print('4 - Unix')
    print('5 - Outros')
    print('0 - Sair do programa')
    print(75*'=')
    resposta = input('Digite a sua resposta: ')
    sys('cls')

    while resposta != '1' and resposta != '2' and resposta != '3' and resposta != '4' and resposta != '5' and resposta != '0':
        sys('cls')
        print(75*'=')
        print(f'Participante {participante}')
        print(75*'=')
        print('Qual o melhor Sistema Operacional em sua opinião?')
        print('1 - Windows')
        print('2 - Linux')
        print('3 - MacOS')
        print('4 - Unix')
        print('5 - Outros')
        print('0 - Sair do programa')
        print(75*'=')
        print('Digito Inválido! (1, 2, 3, 4, 5, 0)')
        resposta = input('Digite a sua resposta: ')
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
            loop_resposta = True
            total_respostas = sistemas[0][1] + sistemas[1][1] + sistemas[2][1] + sistemas[3][1] + sistemas[4][1]

    if total_respostas == 0:
        sim_ou_nao = str()
        while loop_resposta == True:
            sys('cls')
            print('Não tem como fazer uma pesquisa com 0 participantes!')
            print('Deseja tentar novamente? S/N: ')
            sim_ou_nao = str(input('Digite a sua resposta: ')).strip().upper()

            while sim_ou_nao != 'S' and sim_ou_nao != 'N':
                sys('cls')
                print('Não tem como fazer uma pesquisa com 0 participantes!')
                print('Deseja tentar novamente? S/N: ')
                print('Digito Inválido! (S ou N)')
                sim_ou_nao = str(input('Digite a sua resposta: '))

            if sim_ou_nao == 'S':
                loop_resposta = False
                loop_principal = True
            else:
                loop_principal = False
                loop_resposta = False
    else:
        sistemas[0].append(sistemas[0][1] / total_respostas * 100) # Windows
        sistemas[1].append(sistemas[1][1] / total_respostas * 100) # Linux
        sistemas[2].append(sistemas[2][1] / total_respostas * 100) # MacOS
        sistemas[3].append(sistemas[3][1] / total_respostas * 100) # Unix
        sistemas[4].append(sistemas[4][1] / total_respostas * 100) # Outros

        sys('cls')
        print(75*'=')
        print(f'Total de participantes = {total_respostas}')
        print(f'Windows {sistemas[0][1]} - {sistemas[0][2]:.1f}%')
        print(f'Linux {sistemas[1][1]} - {sistemas[1][2]:.1f}%')
        print(f'MacOS {sistemas[2][1]} - {sistemas[2][2]:.1f}%')
        print(f'Unix {sistemas[3][1]} - {sistemas[3][2]:.1f}%')
        print(f'Outros {sistemas[4][1]} - {sistemas[4][2]:1f}%')
        print(75*'=')



