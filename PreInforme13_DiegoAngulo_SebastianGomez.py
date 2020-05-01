# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:41:17 2020

@author: Diego
"""


def promedios(plan):
    
    prom_plan={estudiante:round(sum(plan[estudiante])/len(plan[estudiante]),2) for estudiante in plan}
    
    return prom_plan


def aprobados(plan):
    prom=promedios(plan)
    apr={estudiante:prom[estudiante] for estudiante in prom if prom[estudiante]>=3.0 }
    
    return apr
         
    


planilla={'Pepito':[5.0,3.8,4.2,3.3],'Julian':[5.0,5.0,4.5,4.6],'Sebastian':[3.8,2.2,2.5,3.5],'Jose':[2.0,1.8,3.4,1.7]}

n=int(input('Ingrese 1 si desea obtener el promedio de cada estudiante \nIngrese'
          ' 2 si desea ver las notas de cada estudiante\n'
          'Ingrese 3 si desea ver los alumnos aprobados: '))

if n==1:
    prom_plan=promedios(planilla)
    for estudiante in prom_plan:
        print(estudiante+':',prom_plan[estudiante])
    
elif n==2:
    for estudiante in planilla:
        print(estudiante+':',planilla[estudiante])

elif n==3:
    apr=aprobados(planilla)
    for estudiante in apr:
        print(estudiante+':',apr[estudiante])
    
