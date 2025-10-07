import random

aluno = str(input('insira o nome do primeiro aluno: '))
aluno2 = str(input('insira o nome do segundo aluno: '))
aluno3 = str(input('insira o nome do terceiro aluno: '))
aluno4 = str(input('insira o nome do quarto aluno:  '))

lista = [aluno,aluno2,aluno3,aluno4]

escolha = random.choice(lista)

print(f"O aluno escolhido para apagar o quadro foi {escolha}")
