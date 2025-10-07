import math

catad = float(input('Qual é o valor do cateto adjecente: '))
catop = float(input('Qual é o valor do cateto oposto: '))

hipo = math.hypot(catad,catop)

print(F"A hipotenusa é: {hipo}")