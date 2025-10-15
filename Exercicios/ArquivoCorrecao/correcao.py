'''
    Autores: Glauber Almeida B. - Luis Henrique N. C. Pozenato
    Turma: 2ºA DS               Data: 14/10/2025

    Exercício de fazer o fluxograma de outro grupo
    - Não foi possível fazer o código funcionar seguindo o fluxograma;
    - Portanto, terá alterações dos erros seguindo o documento
'''
from time import sleep
from os import system as sys

confirmacao = 'N'

sys('cls')

print(50*'=')
print('Seja muito bem vindo!!')
print('Aqui você irá digitar 5 números. O programa dirá:')
print('-> O maior número')
print('-> O menor número')
print(50*'=')
input('Pressione ENTER para continuar...')

while confirmacao == 'N':
    lista = []
    contador = 0

    sys('cls')

    while contador != 5:
        lista.append(int(input(f'Digite o {contador+1} número -> ')))
        while type(lista[contador]) != int:
            print('Digito Inválido! Tente novamente.')
            lista.append(int(input(f'Digite o {contador+1} número -> ')))
        contador += 1

    maior = lista[0]
    menor = lista[0]

    for c in range(len(lista)):
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]      

    sys('cls')

    for c in range(0, 7):
        for c in range(0, 3):
            print('.', end='', flush=True)
            sleep(0.15)
        sys('cls')

    print(25*'=')
    print(f'O maior número é: {maior}')
    print(f'O menor número é: {menor}')
    print(25*'=')

    confirmacao = input('Deseja sair do programa? S/N -> ').upper()

    while confirmacao != 'S' and confirmacao != 'N':
        sys('cls')
        print('Digito Inválido, Tente novamente!')
        confirmacao = input('\nDeseja sair do programa? S/N -> ').upper()

sys('cls')
sleep(1)

print('Obrigado por utilizar o programa.')
print('Saindo em:')

for c in range(5, 0, -1):
    print(c)
    sleep(1)

sys('cls')