import random
import numpy as np
from Nodo import *

class Algoritmo:

    def __init__(self, tamPoblacion, entrada, criterioFin, entradaFin, criterioSeleccion, entradaSeleccion):
        self.tamPoblacion = tamPoblacion
        self.entrada = entrada
        self.noEntrada = len(entrada)
        self.criterioFin = criterioFin
        self.entradaFin = entradaFin
        self.criterioSeleccion = criterioSeleccion
        self.entradaSeleccion = entradaSeleccion



    def ejecutar(self):
        print("Algoritmo corriendo\n")
        generacion = 0
        poblacion = self.inicializarPoblacion()
        fin = self.verificarCriterio(poblacion, generacion)

        #while(fin == None):
            #padres = self.seleccionarPadres(poblacion)
            #poblacion = self.emparejar(padres)
            #generacion += 1
            #fin = self.verificarCriterio(poblacion, generacion)
            #imprimirPoblacion(poblacion)
            #print("\n")
            #i += 1

        print("*********** GENERACION ", generacion, " ***************")

        #solucion = [0.45, 0.2, 0.34, 0.15]
        #print(self.evaluarFitness(solucion))



    """
    *   Función que crea la población
    """
    def inicializarPoblacion(self):
        poblacion = []

        for i in range(0, self.tamPoblacion):
            solucion = []
            for j in range(0, 4):
                solucion.append(random.uniform(-2, 2))
            poblacion.append(Nodo(solucion, self.evaluarFitness(solucion)))

        return poblacion



    """
    *   Función que verifica si el algoritmo ya llegó a su fin
    """
    def verificarCriterio(self, poblacion, generacion):
        result = None
        
        if self.criterioFin == 0:
            #maximo numero de generaciones
            if generacion >= self.entradaFin:
                result = True
        
        if self.criterioFin == 1:
            #minimo numero fitness
            for i in range(0, self.tamPoblacion):
                if poblacion[i].fitness >= self.entradaFin:
                    result = True
                    break

        if self.criterioFin == 2:
            #Un porcentaje de la población que tenga un valor fitness igual
            suma_total = 0

            for nodo in poblacion:
                if round(nodo.fitness) == self.entradaFin:
                    suma_total += 1
            
            if (suma_total / len(poblacion)) >= 0.80:
                result = True
            
        return result



    """
    *   Función que evalúa qué tan buena es una solución, devuelve el valor fitness de la solución
    *   @solucion = el número viene en un arreglo como este [0, 1, 1, 1, 0]
    """
    def evaluarFitness(self, solucion):
        # Recorrer el numero de entradas
        for i in range(0, self.noEntrada):
            # obtener fila
            fila = self.entrada[i]
            # calcular nc
            fila[5] = self.calcularNota(solucion, fila)
            # modificar fila
            self.entrada[i] = fila

        return self.calcularError()



    def calcularNota(self, solucion, fila):
        # calcular nc = w1*P1 + w2*p2 + w3*p3 + w4*p4
        nc = 0.0
        for i in range(0, 4):
            w = solucion[i]
            p = fila[i]
            nc += w * p
        return nc



    def calcularError(self):
        # Recorrer el numero de entradas
        # (x1 - x2) ^ 2
        valor = 0.0
        for i in range(0, self.noEntrada):
            fila = self.entrada[i]
            valor += ((fila[4] - fila[5]) ** 2)
        return valor / 4



    """
    *   Función que toma a los mejores padres para luego crear una nueva generación
    """
    def seleccionarPadres(self, poblacion):
        mejoresPadres = []

        if self.criterioSeleccion == 0:
            #Selección aleatoria
            print("0")

        if self.criterioSeleccion == 1:
            #Selección de los padres con mejor valor fitness
            print("1")

        if self.criterioSeleccion == 2:
            #Selección de padres en posiciones impares o solo en posiciones pares
            print("2")

        return mejoresPadres



    """
    *   Función que toma a los mejores padres y genera nuevos hijos
    """
    def emparejar(self, padres):
        return padres




    """
    *   Función que toma dos soluciones padres y las une para formar una nueva solución hijo
    *   Se va a alternar los bits de ambos padres
    *   Se va a tomar un bit del padre 1, un bit del padre 2 y así sucesivamente
    """
    def cruzar(self, padre1, padre2):
        return padre1



    """
    *   Función que toma una solución y realiza la mutación
    *   Se va a cambiar el bit con valor 0 más a la izquierda por 1
    """
    def mutar(self, solucion):
        solucion = solucion.solucion
        return solucion
