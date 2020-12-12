from Algoritmo import *

tamPoblacion = 10

"""
    0 - Un valor minimo alcanzado por una solucion de la poblacion
    1 - Maximo numero de generaciones
    2 - Un porcentaje de la población que tenga un valor fitness igual
"""
criterioFin = 2
entradaFin = 100

"""
    0 - Selección aleatoria
    1 - Selección de los padres con mejor valor fitness
    2 - Selección de padres en posiciones impares o solo en posiciones pares
"""
criterioSeleccion = 0
entradaSeleccion = 10

entrada = []
entrada.append([75, 50, 90, 65, 71.75, 0])
entrada.append([80, 95, 88, 80, 84.65, 0])
entrada.append([20, 55, 60, 58, 52.45, 0])
entrada.append([60, 28, 69, 50, 53.9, 0])

algoritmo = Algoritmo(tamPoblacion, entrada, criterioFin, entradaFin, criterioSeleccion, entradaSeleccion)
algoritmo.ejecutar()