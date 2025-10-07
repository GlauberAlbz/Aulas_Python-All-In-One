'''
    Autores: Glauber Almeida B. - Luis Henrique Nunes C. P.
    Turma: 2ºA DS               Data: 04/09/2025

    Exercício 03
    - Faça um programa que pergunte qual KM de saída do veículo, depois pergunte a KM chegada.
    - Pregunte que horas ele saiu e que horas ele chegou.
    - Calcular qual foi a velocidade média que ele andou
    - Se ele andou acima de 80km/h = multa de R$ 5,00 por KM.

'''

import datetime as dt
import os

os.system('cls')

inicio = float(input("Qual o km de inicio? "))
chegada = float(input("Qual o km de chegada? "))
multa = int()

print("Horárido de saída: (primeiro responda o horário e depois os minutos) ")
hora_ini = int(input("Horas: "))
minuto_ini = int(input("Minutos: "))

print("Horárido de chegada: (primeiro responda o horário e depois os minutos) ")
hora_fim = int(input("Horas: "))
minuto_fim = int(input("Minutos: "))


# Conversão de valores e cálculos físicos (criei essa parte para fazer os cálculos físicos)

delta_hora = hora_fim - hora_ini
delta_minuto = minuto_fim - minuto_ini
conversao_minuto = delta_minuto / 60 # Converte minutos em horas, exemplo: 30 minutos = 0,5 horas
conversao_horas = delta_hora + conversao_minuto

deltaS = chegada - inicio
deltaT = conversao_horas

velocidade_media = deltaS / deltaT



print(50*"-")
print(f"Quantidade de kilômetros rodados: {deltaS:.2f}KM")
print(f"Tempo de viagem: {delta_hora}:{delta_minuto}h")
print(f"Velocidade média: {velocidade_media:.0f}Km/h")
if velocidade_media > 80:
    multa = 5 * deltaS
    print(f"Você excedeu o limite de velocidade(80km/h), portando deverá pagar uma multa de: R${multa:.2f}")
else:
    print(f"Sem multas.")
print(50*"-")