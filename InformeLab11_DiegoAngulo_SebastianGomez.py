# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:54:25 2020

@author: Diego
"""

from random import randint

import numpy as np

def generador(minimo,maximo):
     
    lista=[[0]*12 for i in range(4)] 
    arreglo=np.array(lista)
    fila,columna=arreglo.shape

    for j in range(0,fila):
        for i in range(0,columna):
            
            arreglo[j][i]=randint(minimo,maximo)
    
    return arreglo


def imprimir(arreglo):
    ciudades=['Bucaramanga','FLoridablanca', 'Giron', 'Piedecuesta']
    ciudad=np.array(ciudades)
    
    meses=['Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic']
    
    print('            ' +str(meses))
    fila,columna=arreglo.shape
    for i in range(0,fila):
        print(ciudad[i],arreglo[i])
        
        
def restador(a,b):
    
    filas,columnas=a.shape
    
    R=[[0]*columnas for col in range(filas)]
    r=np.array(R)
    
    for i in range(filas):
        for j in range(columnas):
            r[i][j]=a[i][j]-b[i][j]
    
    return r
        

def mejor_ciudad(ganancias):
    ciudad=['Bucaramanga','FLoridablanca','Giron','Piedecuesta']
    ganTotal=[0]*4
    fila,columna=ganancias.shape
    mayor=ganTotal[0]
    
    
    
    for i in range(fila):
        
        for j in range(columna):
            ganTotal[i]=ganTotal[i]+ganancias[i][j]
            if ganTotal[i]>mayor:
                mayor=ganTotal[i]
     
    size=len(ganTotal)
    
    for i in range(size):
        if ganTotal[i]==mayor:
            print('La ciudad con mayor ganancia fue '+str(ciudad[i])+' con '+str(ganTotal[i])+' millones COP')
            
            
def peor_ciudad(ganacias):
    ciudad=['Bucaramanga','FLoridablanca','Giron','Piedecuesta']
    perTotal=[0]*4
    fila,columna=ganancias.shape
    menor=0
    
    
    
    for i in range(fila):
        
        for j in range(columna):
            perTotal[i]=perTotal[i]+ganancias[i][j]
        if menor==0:
            menor=perTotal[i]
        if perTotal[i]<menor:
            menor=perTotal[i]
    print(perTotal)
    
     
    size=len(perTotal)
    
    for i in range(size):
        if perTotal[i]==menor:
            print('La ciudad con menor ganancia fue '+str(ciudad[i])+' con '+str(perTotal[i])+' millones COP')
    
    
def 
    
#------------------------------Main-------------------------------#       
    


ingresos=generador(100,180)
egresos=generador(60,130)

ganancias=restador(ingresos, egresos)
print('         Ingresos      ')
imprimir(ingresos)
print()
print('         Egresos       ')
imprimir(egresos)
print()
print('         Ganancias        ')
imprimir(ganancias)
print()
mejor_ciudad(ganancias)
peor_ciudad(ganancias)




