# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:49:49 2020

@author: Diego
"""


import numpy as np


def valorInv(inv, cant):   #Calcula el valor del inventario
    acum=0
    for i in range (0, cant):
        
        valPro=int(inv[i][1])*int(inv[i][2])
        acum=acum+valPro
    
    print('El valor total del inventario es '+str(acum))

def cantInv(inv, cant):    #Calcula la cantidad total del inventario
    
    acum=0
    for i in range (0,cant):
        
        cantPro=int(inv[i][2])
        acum=acum+cantPro
        
    print('La cantidad total de articulos en stock es '+str(acum))
    

cant = int(input(print('Ingrese la cantidad de productos que desea enlistar: ')))

lista=[['holaaaaaaaaaaaa']*3 for i in range(cant)]     #Se coloca una palabra larga ya que si el dato 
inv=np.array(lista)                                    #sobrepasa la palabra que ya esta en la lista, solo guarda la misma cantidad de letras                     

for i in range (0, cant):    #Ingresa los datos de los productos
    b=i+1
    
    producto=input('Ingrese el nombre del producto '+str(b)+': ')
    inv[i][0]=producto
    
    precio=str(input('Ingrese el precio del producto '+str(b)+': '))
    inv[i][1]=precio
    
    stock=str(input('Ingrese la cantidad en stock del producto '+str(b)+': '))
    inv[i][2]=stock
    
print(inv)

valorInv(inv, cant)
cantInv(inv, cant)

       
    
