# Autores: Glauber Almeida, Luis Henrique Nunes
# 

import math

ang = math.radians(float(input('Qual angulo deseja verificar?: ')))


cos = math.cos(ang)
sen = math.sin(ang)
tan = math.tan(ang)

print(f"O coseno é {cos:.2f}, o seno é  {sen:.2f}, a tangente {tan:.2f}")