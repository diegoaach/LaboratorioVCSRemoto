# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:24:41 2020

@author: Diego
"""
#%% Invertir un numero
n = int(input('Ingrese un numero de 4 cifras: '))
n = abs(n)
inverso = 0

while n>0:
    inverso = (inverso*10) + (n%10)
    n = n//10

print (inverso)

#%% Filas progresivas

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



#%%
def mi_funcion():
    print('Hola mundo')
    

mi_funcion()