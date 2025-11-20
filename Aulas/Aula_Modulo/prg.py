import calc
from os import system
system("cls")

num = int(input("Digite um valor: "))

fat = calc.fatorial(num)
dob = calc.dobro(num)
trip = calc.triplo(num)

print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dob}")
print(f"O triplo de {num} é {trip}")