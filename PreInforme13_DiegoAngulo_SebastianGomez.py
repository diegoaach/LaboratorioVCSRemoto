# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:41:17 2020

@author: Diego
"""


def promedios(plan):
    
    prom_plan={estudiante:round(sum(plan[estudiante])/len(plan[estudiante]),2) for estudiante in plan}
    
    for estudiante in prom_plan:
        print(estudiante+':',prom_plan[estudiante])


planilla={'Pepito':[5.0,3.8,4.2,3.3],'Julian':[5.0,5.0,4.5,4.6],'Sebastian':[3.8,2.2,2.5,3.5]}

n=int(input('Ingrese 1 si desea obtener el promedio de cada estudiante \nIngrese'
          ' 2 si desea ver las notas de cada estudiante: '))

if n==1:
    promedios(planilla)
elif n==2:
    for estudiante in planilla:
        print(estudiante+':',planilla[estudiante])
