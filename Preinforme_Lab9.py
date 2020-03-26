# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:24:41 2020

@author: Diego
"""

n = int(input('Ingrese el numero de filas que desea imprimir: '))

contn = 0
fila = 0
nf = 1
while contn<n:
    
    fila = fila*10 + nf
    nf += 1
    contn += 1
    print(fila)
    
    if nf>9:
        nf = 0

print('Filas completadas: ',contn)

