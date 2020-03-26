# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:49:36 2020

@author: Sebastian
"""

contkg=0
# Este while sirve para que mientras el avion no llegue al 95% de su capacidad maxima siga recibiendo paquetes
while contkg<237000:
    print("Ingrese la distancia del envio del paquete y su peso")
    km= float(input("Distancia: "))
    kg= float(input("Peso: "))
    if kg>10:
        # Aqui se esta definiendo que descuentos se aplicaran mediante condicionales
        print("¿El vuelo es intercontinental? Si/no")
        dec= str(input("Vuelo intercontinental:"))
        if dec=="si":
            ml= km/1.6
            pi= kg*4500+ml*8000
            if km>8000 and kg>400:
                pfi= pi*0.9
            else:
                pfi= pi
        else:
            pi=kg*4500+km*4000
            if kg>100:
                pfi= pi*0.85
            else:
                pfi= pi
        print("El precio del envio es: ", (pfi))
        contkg=contkg+kg
    else:
        print("El peso no es aceptable")
else:
    print("El avion esta a su maxima capacidad")