# Ecuación de segundo grado usando funciones

import math 
"""Las variables a , b y c en el programa principal no son las mismas que en la función hallar_discriminante donde 
corresponden a a1, b1 y c1"""

def hallar_driscriminante(a1, b1, c1):
    d = math.sqrt(b1*b1 - 4*a*c)
    return d

# Programa principal
a = float(input("Coeficiente de x²"))
b = float(input("Coeficiente de x"))
c = float(input("Termino independiente"))

#Calculo del discriminante
d1 = hallar_driscriminante(a, b, c)

#Se calculan las raices
x1 = (-b + d1)/2*a
x2 = (-b - d1)/2*a

#Resultados
print("Primera raíz: " ,x1)
print("Primera raíz: " ,x2)