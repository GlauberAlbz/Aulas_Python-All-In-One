'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 28/08/2025

    1) Pegue a data de nascimento do usuário, fale quantos anos ele tem, depois fale quantos anos ele terá em 2050.
'''

import datetime as dt

data_atual = dt.date.today()

print(f"Insira sua data de nascimento:")
dia = int(input("Dia em que nasceu: "))
mes = int(input("Mês em que nasceu: "))
ano = int(input("Ano em que nasceu: "))

user_nascimento = dt.date(day = dia, month=mes, year=ano)
user_idade_dias = data_atual - user_nascimento 
user_idade_anos = user_idade_dias / 365
user_idade_futuro = user_idade_anos.days + 25

print(f"Você tem {user_idade_anos.days} anos.")
print(f"Você terá {user_idade_futuro} anos em 2050.")
