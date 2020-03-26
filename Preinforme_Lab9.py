# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:24:41 2020

@author: Diego
"""


n = int(input('Ingrese un numero de 4 cifras: '))
n = abs(n)
inverso = 0

while n>0:
    inverso = (inverso*10) + (n%10)
    n = n//10

print (inverso)
