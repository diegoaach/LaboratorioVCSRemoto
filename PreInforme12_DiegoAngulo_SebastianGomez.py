# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:29:12 2020

@author: Diego
"""

def difMayorMenor(datos): #Restara el mayor dato menos el menor dato registrado en la lista
    size=len(datos)
    mayor=datos[0]
    menor=datos[0]
    
    for i in range(size): #Este for se usa para ubicar el mayor y menor dato
        if datos[i]>mayor:
            mayor=datos[i]
        
        if datos[i]<menor:
            menor=datos[i]
    
    dif=mayor-menor #La resta
    print('La diferencia entre el mayor y el menor dato es '+str(round(dif,2)))
    
    

def promedio(datos): #Saca el promedio de los datos de la lista
    
    suma =0
    prom=0
    size=len(datos)
    
    for i in datos: #Se suman todos los datos
        suma=suma+i
    
    prom=round(suma/size,3)  #Se divide el total de la suma entre la cantidad de datos
    
    return prom
    

def devStd(datos): #Calcula la desviacion estandar de la lista completa(poblacion)
    
    prom=promedio(datos)
    size=len(datos)
    acum=0
    
    for i in range(size):  #Sumatorio del cuadrado de la diferencia entre el dato y la media
        acum=acum+((datos[i]-prom)**2)
    
    desv=round((acum/size)**(1/2),3)   #Raiz cuadrada de la sumatoria sobre la cantidad de los datos
    
    return desv


def mediana(datos):  #Calcula la mediana de los datos
    
    arreglado=datos.copy()
    arreglado.sort()
    size=len(arreglado)
    med=0
    if size%2==0:        #Si la cantidad de los datos es par, el proceso es diferente a si es impar
        ind=int(size/2)
        med=(arreglado[ind]+arreglado[ind+1])/2
    else:
        ind=int(round((size/2),0))
        med=arreglado[ind]
        
    return med


def semConse(datos):    #Calcula las semanas consecutivas en que las presiones 
                        #fueron menores o mayores a la media en una sola lista
    
    prom=promedio(datos)
    size=len(datos)
    conse=[]
    
    for i in range(0,size-1):
        if (datos[i]>prom and datos[i+1]>prom) or (datos[i]<prom and datos[i+1]<prom):
            conse.append(datos[i])
    
    return conse


def temperatura(datos):  #Calcula la temperatura segun la ley de los gases ideales
    temp=[]
    n=17.16
    R=8.314472
    V=510
    size=len(datos)
    
    for i in range(size):
        temp.append(round((((datos[i]*V)/(n*R)-273.15)),2))
                    
    return temp   

def conseTemp(temp):        #Obtiene las semanas que la temperatura esta sobre o por debajo
    prom=promedio(datos)    #de la media y las separa en 2 listas, que conforman una sola
    size=len(datos)
    conse=[]
    porEncima=[]
    porDebajo=[]
    
    
    
    for i in range(0,size-1):
        if (datos[i]>prom and datos[i+1]>prom):
            porEncima.append(datos[i])
            
        elif (datos[i]<prom and datos[i+1]<prom):
            porDebajo.append(datos[i])
            
        
    
    conse=[porEncima, porDebajo]
    
    return porEncima, porDebajo, conse
            
    

        


    

datos = [110.06,107.89,108.45,108.49,109.03,110.11,109.87,119.38,119.35,116.34,117.73,120.01,118.19,119.53,117.09,118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,110.67,107.73,105.76,107.85]

difMayorMenor(datos)

prom=promedio(datos)
print('Promedio anual: ' +str(prom))
desv=devStd(datos)
print('Desviacion estandar: '+str(desv))
med=mediana(datos)
print('Mediana: '+str(med))
conse=semConse(datos)
print('Datos de las semanas consecutivas: \n'+str(conse))

temp=temperatura(datos)
print('Temperatura: '+str(temp))

desvTemp=devStd(temp)
print('Desviacion de la temperatura: '+str(desvTemp))
porEncima,porDebajo,conseT=conseTemp(temp)

desvArriba=devStd(porEncima)
print('Desviacion de las temperaturas consecutivas por encima de la media: '+str(desvArriba))

desvAbajo=devStd(porDebajo)
print('Desviacion de las temperaturas consecutivas por debajo de la media: '+str(desvAbajo))
medDesv=(desvArriba+desvAbajo)/2
print('Media de las desviaciones: '+str(medDesv))

difMayorMenor(temp)











