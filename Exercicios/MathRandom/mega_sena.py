import random

n1 = int(input("Digite o primeiro número de 1 a 60 "))
n2 = int(input("Digite o segundo número de 1 a 60 "))
n3 = int(input("Digite o terceiro número de 1 a 60 "))
n4 = int(input("Digite o quarto número de 1 a 60 "))
n5 = int(input("Digite o quinto número de 1 a 60 "))
n6 = int(input("Digite o sexto número de 1 a 60 "))

ale1 = random.randint(1, 60)
ale2 = random.randint(1, 60)
ale3 = random.randint(1, 60)
ale4 = random.randint(1, 60)
ale5 = random.randint(1, 60)
ale6 = random.randint(1, 60)

print(f"\nSeus números foram: [{n1} {n2} {n3} {n4} {n5} {n6}]")
print(f"Os números sorteados foram: [{ale1} {ale2} {ale3} {ale4} {ale5} {ale5}]\n")
