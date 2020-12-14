from Algoritmo import *
import datetime
import time


"""
    0 - Maximo numero de generaciones
    1 - Un valor minimo alcanzado por una solucion de la poblacion
    2 - Un porcentaje de la población que tenga un valor fitness igual
"""
criterioFin = 0

"""
    0 - Selección aleatoria
    1 - Selección de los padres con mejor valor fitness
    2 - Selección de padres en posiciones impares o solo en posiciones pares
"""
criterioSeleccion = 1

entrada = []
entrada.append([75, 50, 90, 65, 71.75, 0])
entrada.append([80, 95, 88, 80, 84.65, 0])
entrada.append([20, 55, 60, 58, 52.45, 0])
entrada.append([60, 28, 69, 50, 53.9, 0])

algoritmo = Algoritmo()
algoritmo.entrada = entrada
algoritmo.criterioFin = criterioFin
algoritmo.criterioSel = criterioSeleccion
#algoritmo.ejecutar()

today = datetime.datetime.now()
print(today)
print('ctime  :', today.ctime())

print(time.time())

print ("Fecha " + time.strftime("%x"))
print ("hora " + time.strftime("%X"))
