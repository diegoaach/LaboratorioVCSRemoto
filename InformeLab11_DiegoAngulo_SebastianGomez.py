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
    ciudades=['Bucaramanga    ','FLoridablanca  ', 'Giron          ', 'Piedecuesta    ']
    ciudad=np.array(ciudades)
    
    meses=['Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic']
    
    print('             ' +str(meses))
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
    
    
def mejor_mes(ganancias):
    
    mes=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    ciudades=['Bucaramanga','Floridablanca','Giron','Piedecuesta']
    
    fila,columna=ganancias.shape
    
    for i in range(fila):
        mejor=[i][0]
        for j in range(columna):
            if ganancias[i][j]>mejor:
                mejor=ganancias[i][j]
                ind=j
        
        print('El mejor mes de '+str(ciudades[i])+' fue '+str(mes[ind])+' con '+str(mejor)+' millones COP')
    
    
def peor_mes(ganancias):
    
    mes=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    ciudades=['Bucaramanga','Floridablanca','Giron','Piedecuesta']
    
    fila,columna=ganancias.shape
    
    for i in range(fila):
        peor=ganancias[i][0]
        for j in range(columna):
            if ganancias[i][j]<peor:
                peor=ganancias[i][j]
                ind=j
        
        print('El peor mes de '+str(ciudades[i])+' fue '+str(mes[ind])+' con '+str(peor)+' millones COP')   
    

def imprimir_perso(arreglo,a,b):
    mes=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
    ciudades=['Bucaramanga   ','Floridablanca ' ,'Giron         ','Piedecuesta   ']
    fila,columna=arreglo.shape    
    
    print('              ' +str(mes[a-1:b]))

    for i in range(fila):
        print(ciudades[i],arreglo[i][a-1:b])

def promedio(ingresos,egresos,ganancias):
    ciudades=['Bucaramanga','Floridablanca','Giron','Piedecuesta']
    fila,columna=ingresos.shape
    
    print('--------Promedio Ingresos----------')
    for i in range(fila):
        acum=0
        for j in range(columna):
            acum=acum+ingresos[i][j]
        prom=acum/columna
        
        print(ciudades[i],round(prom,3))
    
    print('--------Promedio Egresos----------')
    for i in range(fila):
        acum=0
        for j in range(columna):
            acum=acum+egresos[i][j]
        prom=acum/columna
        
        print(ciudades[i],round(prom,3))
    
    print('--------Promedio Ganancias----------')
    for i in range(fila):
        acum=0
        for j in range(columna):
            acum=acum+ganancias[i][j]
        prom=acum/columna
        
        print(ciudades[i],round(prom,3))
        
        
def extraer_proporciones(ganancias):
    ciudades=['Bucaramanga','Floridablanca','Giron','Piedecuesta']
    fila,columna=ganancias.shape
    
    
    for i in range(fila):
        contPer=0
        contGan=0
        for j in range(columna):
            if ganancias[i][j]<0:
                contPer+=1
            else:
                contGan+=1
        
        porc=(contPer*100)/12
        print('EL porcentaje de perdida en '+str(ciudades[i])+' es '+str(round(porc,3))+'% y '+str(round(100-porc,3))+'% de ganancia')
                
            
#------------------------Punto 9----------------------#

def generador3d(ingresos,egresos):
    fila,columna=ingresos.shape
    
    p1=9.5
    p2=5.6
    
    ingreso3d=[[[0 for x in range(columna)] for i in range(fila)]for j in range(5) ]
    ingreso3d[0]=ingresos 
    
    for i in range(1,5):
       for j in range(fila):            
            for k in range(columna):                
                ingreso3d[i][j][k]=round((ingresos[j][k]*100)/(100+p1),1)
                
    egreso3d=[[[0 for x in range(columna)] for i in range(fila)]for j in range(5) ]
    egreso3d[0]=egresos    
    
    for i in range(1,5):
        for j in range(fila):
            for k in range(columna):
                egreso3d[i][j][k]=round((egresos[j][k]*100)/(100+p2),1)
    
    ingresos3d=np.array(ingreso3d)
    egresos3d=np.array(egreso3d)
    
    
    
    return ingresos3d, egresos3d

    
def imprimir3d(arreglo):
    
    ciudades=['Bucaramanga   ','Floridablanca ','Giron         ','Piedecuesta   ']
    meses=['Ene   Feb   Mar   Abr   May   Jun   Jul   Ago   Sep   Oct   Nov   Dic']
    year=2019
    dim,fila,columna=arreglo.shape
    
    print('              '+str(meses))
    
    for i in range(dim):
        print('Año '+str(year))
        year=year-1
        print()
        for j in range(fila):
            print(ciudades[j],arreglo[i][j])
        print()


def ganancias3d(ingresos,egresos):
    
    dim,fila,columna=ingresos.shape
    ganancia=[[[0 for x in range(columna)] for i in range(fila)]for j in range(dim)]
    ganancias=np.array(ganancia)
    
    for i in range(dim):
        for j in range(fila):
            for k in range(columna):
                ganancias[i][j][k]=ingresos[i][j][k]-egresos[i][j][k]
    
    return ganancias
                
    
    
                
    
               
    
    
    
    
    
        
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
print()
mejor_mes(ganancias)
print()
peor_mes(ganancias)
print()

a=int(input('Ingrese el mes a iniciar (numero): '))
b=int(input('Ingrese el mes a finalizar (numero): '))
print()
imprimir_perso(ingresos, a, b)
print()
imprimir_perso(egresos, a, b)
print()
imprimir_perso(ganancias, a, b)
print()
promedio(ingresos,egresos,ganancias)
print()
extraer_proporciones(ganancias)

print()
ingresos3d,egresos3d=generador3d(ingresos,egresos)
print()
print('------------Ingresos entre 2015 y 2019-------------')
imprimir3d(ingresos3d)
print('------------Egresos entre 2015 y 2019-------------')
imprimir3d(egresos3d)

print()
ganancia3d=ganancias3d(ingresos3d,egresos3d)
print('-----------------Ganancias entre 2015 y 2019---------------')
imprimir3d(ganancia3d)







#mes=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']
#ciudades=['Bucaramanga','Floridablanca','Giron','Piedecuesta']

