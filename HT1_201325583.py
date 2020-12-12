import random
import numpy as np

class Nodo:
    def __init__(self, solucion = [], fitness = 0):
        self.solucion = solucion
        self.fitness = fitness



def ejecutar():
    print("Algoritmo corriendo\n")
    generacion = 0
    poblacion = inicializarPoblacion()
    fin = verificarCriterio(poblacion, generacion)

    #i = 0
    while(fin == None):
    #while i < 10 :
        padres = seleccionarPadres(poblacion)
        poblacion = emparejar(padres)
        generacion += 1
        fin = verificarCriterio(poblacion, generacion)
        imprimirPoblacion(poblacion)
        print("\n")
        #i += 1

    print("*********** GENERACION ", generacion, " ***************")
    imprimirPoblacion(poblacion)
    print(fin)



def inicializarPoblacion():
    poblacion = []

    for i in range(0, 10):
        solucion = []
        for j in range(0, 8):
            solucion.append(random.randint(0, 9))
        poblacion.append(Nodo(solucion, evaluarFitness(solucion)))
        
    return poblacion



def verificarCriterio(poblacion, generacion):
    result = None

    for i in range(0, 10):
        if poblacion[i].fitness >= 7:
            return True

    return result



def evaluarFitness(solucion):
    valorFitness = 0
    modelo = [1, 5, 7, 8, 6, 9, 3, 4]

    for i in range(0, 8):
        if modelo[i] == solucion[i]:
            valorFitness += 1

    return valorFitness



def seleccionarPadres(poblacion):
    mejoresPadres = []

    ordenDescendente = sorted(poblacion, key= lambda item: item.fitness, reverse=True)
    for i in range(0, 5):
        mejoresPadres.append(ordenDescendente[i])

    return mejoresPadres



def emparejar(padres):
    nuevaPoblacion = padres

    #   union P1 P2
    hijo1 = Nodo([], 0)
    hijo1.solucion = cruzar(padres[0].solucion, padres[1].solucion)
    hijo1.solucion = mutar(hijo1)
    hijo1.fitness = evaluarFitness(hijo1.solucion)

    #   union P3 P5
    hijo2 = Nodo([], 0)
    hijo2.solucion = cruzar(padres[2].solucion, padres[4].solucion)
    hijo2.solucion = mutar(hijo2)
    hijo2.fitness = evaluarFitness(hijo2.solucion)

    #   union P1 P3
    hijo3 = Nodo([], 0)
    hijo3.solucion = cruzar(padres[0].solucion, padres[2].solucion)
    hijo3.solucion = mutar(hijo3)
    hijo3.fitness = evaluarFitness(hijo3.solucion)

    #   union P3 P4
    hijo4 = Nodo([], 0)
    hijo4.solucion = cruzar(padres[2].solucion, padres[3].solucion)
    hijo4.solucion = mutar(hijo4)
    hijo4.fitness = evaluarFitness(hijo4.solucion)

    #   union P1 P5
    hijo5 = Nodo([], 0)
    hijo5.solucion = cruzar(padres[0].solucion, padres[4].solucion)
    hijo5.solucion = mutar(hijo5)
    hijo5.fitness = evaluarFitness(hijo5.solucion)

    nuevaPoblacion = [hijo1, hijo2, hijo3, hijo4, hijo5, padres[0], padres[1], padres[2], padres[3], padres[4]]

    return nuevaPoblacion



def cruzar(padre1, padre2):
    # padre1 = [], padre2 = []
    hijo = [padre2[0], padre2[1], padre1[2], padre1[3], padre2[4], padre2[5], padre1[6], padre1[7]]
    return hijo



def mutar(solucion):
    solucion = solucion.solucion

    for i in range(0, 8):
        if random.random() >= 0.5:
            solucion[i] = random.randint(0, 9)

    return solucion



def imprimirPoblacion(poblacion):
    i = 0
    while i < len(poblacion):
        print(poblacion[i].solucion, " ", poblacion[i].fitness)
        i += 1



ejecutar()