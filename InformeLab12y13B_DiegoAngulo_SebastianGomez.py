# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:16:08 2020

@author: Diego
"""
import random as random

def combinar(ponderado,simbolos):
    size=len(simbolos)
    for i in range(size):
        baraja={peso+str(simbolos[i]):ponderado[peso] for i in range(size) for peso in ponderado}
    
    return baraja

def revolver(baraja1):
    size=len(baraja1)
    keys=list(baraja1.keys())
    baraja={}
    for i in range(size):
        key=random.choice(keys)
        
        baraja[key]=baraja1[key]
        keys.remove(key)
    return baraja

def repartir(jug,cartas):
    
    if len(jug)==0:
        for i in range(2):
            carta_u=random.choice(cartas)
            jug.append(carta_u)
            cartas.remove(carta_u)    
    elif len(jug)>=2:
        carta_u=random.choice(cartas)
        jug.append(carta_u)
        cartas.remove(carta_u)
    
    return jug


def sumar_cartas(mano,baraja):
    suma=0
    for i in mano:
            suma=suma+baraja[i]
    return suma

def mostrar(mano,suma):
    print(mano)
    print('Valor de la mano: ',suma)
    
    
    
      
        
        
response='0'
#Variables para contabilizar victorias y derrotas al final de cada juego
gano=0
perdio=0


    

   
#Creando el maso---------------------------------------------
peso=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
valor=[1,2,3,4,5,6,7,8,9,10,10,10,10]
size_list=len(peso)
ponderado={peso[i]:valor[i] for i in range(size_list)}
simbolos=['(C)','(D)','(T)','(P)']
baraja=combinar(ponderado, simbolos)
    
    
    
while response == '0' or response=='si':
    if response == 'no':
        break

#Revolviendo el maso------------------------------------------
    baraja=revolver(baraja)
    cartas=list(baraja.keys())

#Empieza el juego----------------------------------------------

    cartas_jugador=[]
    cartas_tallador=[]
    cartas_jugador=repartir(cartas_jugador,cartas)
    
    
    suma_jug=0
    suma_tal=0
    suma_jug=sumar_cartas(cartas_jugador,baraja)
    
    if suma_jug<21:
        while suma_jug<21:
            mostrar(cartas_jugador,suma_jug)
            rep=int(input('Para repartir, oprima 1 \nPara plantarse, oprima 2\n'))
            if rep==1:
                cartas_jugador=repartir(cartas_jugador,cartas)
                suma_jug=sumar_cartas(cartas_jugador,baraja)
            elif rep==2:
                break
        
                  
    if suma_jug==21:
        print('Cartas del jugador')
        mostrar(cartas_jugador, suma_jug)
        gano+=1
        response=(input('Jugador gana. Desea iniciar otra partida?'))
        continue
        
    elif suma_jug>21:
        print('Cartas del jugador')
        mostrar(cartas_jugador, suma_jug)
        perdio+=1
        response=input('Jugador pierde. Desea iniciar otra partida?')
        continue
        
        
    cartas_tallador=repartir(cartas_tallador,cartas)
    suma_tal=sumar_cartas(cartas_tallador,baraja)
    
    while suma_tal<suma_jug and suma_tal < 21:
        cartas_tallador=repartir(cartas_tallador, cartas)
        suma_tal=sumar_cartas(cartas_tallador, baraja)
        
    if suma_tal==21:
        print('Cartas del jugador')
        mostrar(cartas_jugador, suma_jug)
        print('Cartas del tallador')
        mostrar(cartas_tallador, suma_tal)
        perdio+=1
        response=input('Jugador pierde. Desea iniciar otra partida?')
        
        
    elif suma_tal>21:
        print('Cartas del jugador')
        mostrar(cartas_jugador, suma_jug)
        print('Cartas del tallador')
        mostrar(cartas_tallador, suma_tal)
        gano+=1
        response=(input('Jugador gana. Desea iniciar otra partida?'))
        
    
    elif suma_tal>suma_jug:
        print('Cartas del jugador')
        mostrar(cartas_jugador, suma_jug)
        print('Cartas del tallador')
        mostrar(cartas_tallador, suma_tal)
        perdio+=1
        response=input('Jugador pierde. Desea iniciar otra partida?')
        
    
    else:
        print('Cartas del jugador')
        mostrar(cartas_jugador, suma_jug)
        print('Cartas del tallador')
        mostrar(cartas_tallador, suma_tal)
        gano+=1
        response=(input('Jugador gana. Desea iniciar otra partida?'))
        
        
    
        
        
print('Partidas ganadas: ',gano)
print('Partidas perdidas: ',perdio)
print('----------FIN DEL JUEGO----------')
        
        
    
    
    
    
        
    
        
            
            
        











