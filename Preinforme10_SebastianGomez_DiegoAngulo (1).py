# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:37:50 2020

@author: SeGA
"""
import numpy as np

def utilidades():
    util=np.array([27834.00,23789.00,30189.00,30967.00,32501.00,32701.00,31665.00,17155.00,4614.00,834.00])
    return util
## Punto 1
def difMediaInFin(util):
    acum1=0
    acum2=0
    size=len(util)
    for i in range(0,2):
        ut=util[i]
        acum1=acum1+ut
    for i in range(size-1,size-3,-1):
        ut=util[i]
        acum2=acum2+ut
    dif=(acum1/2)-(acum2/2)
    return dif
## Punto 2
def difMinMax(util):
    size= len(util)
    ite= util[0]
    menor=ite
    for i in range(1,size):
        if menor >(util[i]):
            ite = util[i]
            menor = ite
    ite= util[0]
    mayor=ite
    for i in range(1,size):
        if mayor <(util[i]):
            ite = util[i]
            mayor = ite
    dif=mayor-menor
    return dif
## Funcion necesaria para la mediana, ordena los datos de menor a mayor
def ordenar(util):
    for i in range(len(util)):
        mover = i + np.argmin(util[i:])
        (util[i], util[mover]) = (util[mover], util[i])
    return util
## Punto 3
def mediana(utilM):
    size=len(utilM)
    acum=0
    for i in range(0,size):
        ut=utilM[i]
        if i==5 or i==4:
            acum= acum+ut
    mediana=acum/2
    return mediana
## Funcion necesaria para el punto 5, saca la media de las utilidades
def media(util):
    size=len(util)
    acum=0
    for i in range(0,size):
        ut=util[i]
        acum= acum+ut
    media=acum/size
    return media
## Punto 5
def utilOpAcum(util):
    size=len(util)
    acum=0
    for i in range(0,size):
        ut=util[i]
        acum=acum+ut
    for i in range(0,size):
        ut=util[i]
        perUtil=(ut/acum)*100
        util[i]=perUtil
        print("Las utilidades del año:"+str(año[i])+" fue un porcentaje del:"+str(round(util[i],3))+"%")  
## Punto 6
def defi2017(util):
    deficit=util[9]-util[8]   
    return deficit
## Punto 7
def deficitAll(util):
    size=len(util)
    ute=util[0]   
    for i in range(1,size):      
        ut=util[i]
        percen=(ut/ute)*100
        ute=ut 
        util[i]=percen-100
        util[0]=0
        print("El porcentaje de deficit del "+str(año[i])+" con respecto al anterior es de:"+str(round(util[i],3))+"%" )

## Llamado a las funciones

## Declarando util, como el array utilidades
util=utilidades()
año=np.array([2008,2009,2010,2011,2012,2013,2014,2015,2016,2017])
print("La diferencia entre las utilidades de los primeros dos años y de los dos ultimos años es de:"+ str(difMediaInFin(util))+" Millones de COP")

print("La diferencia entre el año que mas utilidades tuvo y el que menos utilidades tuvo es de:"+str(difMinMax(util))+" Millones de COP")

## Declarando utilM, como el array util ordenado de manor a mayor
utilM=ordenar(util)

print("La mediana operacional de los años registrados es de:"+str(mediana(utilM))+" Millones de COP")

media=media(util)

## Se volvio a declarar util como el array utilidades debido a que util se habia alterado su orden
## Declarando como el array utilidades() lo vuelve a su estado original
util=utilidades()

(utilOpAcum(util))

## Se volvio a declarar util como el array utilidades debido a que util se habia convertido en el array de los porcentajes(punto5)
util=utilidades()

print("El deficit del año 2017 con respecto al año anterior es de:"+str(defi2017(util))+" Millones de COP")


(deficitAll(util))






