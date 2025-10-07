import datetime as dt 

'''data = dt.date(2021,9,25)
print(data)

print(50*("-"))

dia = data.day
mes = data.month
ano = data.year

print(dia, mes, ano)

print(50*("-"))
'''

print(f"Digite a ata desejada.")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

data = dt.date(day = dia, month=mes, year=ano)

print(dia,mes,ano, sep="/")

data_atual = dt.date.today()
print(data_atual)