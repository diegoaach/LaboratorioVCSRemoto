# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:49:36 2020

@author: Diego
"""

from math import sqrt
# Aqui se estan pidiendo los 3 numeros de la cuadratica
print("Funcion cuadrática : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
# r es un discriminante, este determina si la cuadratica tiene raices, una,dos o son complejas
r = b**2 - 4*a*c

if r > 0:
    numRaices = 2
    x1 = (((-b) + sqrt(r))/(2*a))     
    x2 = (((-b) - sqrt(r))/(2*a))
    print("Hay dos raices %f y %f" % (x1, x2))
elif r == 0:
    numRaices = 1
    x = (-b) / 2*a
    print("Hay una raiz: ", x)
else:
    numRaices = 0
    print("Las raices no existen, son numeros complejos.")
    