import random
import numpy as np
from Nodo import *
from Singleton import *

class Algoritmo:

    def __init__(self):
        self.entrada            = []
        self.criterioFin        = 0
        self.criterioSel        = 0

        # maximo en generaciones - sel[0, 1, 2]
        self.tamPoblacion       = 20
        self.tamIndividuo       = 4
        self.maxGeneraciones    = 5000
        self.minFitness         = 0.2
        self.espFitness         = 0.2
        self.espPorcentaje      = 0.95
        self.noSelPadres        = 10

        # valor minimo alcanzado - sel[1, 2]
        #self.tamPoblacion       = 20
        #self.tamIndividuo       = 4
        #self.maxGeneraciones    = 5000

        #self.minFitness         = 100   #solo para 2 de sel
        #self.espFitness         = 100   #prueba para porcentaje
        #self.espPorcentaje      = 0.8   #prueba para porcentaje
        
        #self.noSelPadres        = 10


        # todo con maxNumGen termina bien
        # maxNumGen = SelAleatoria  - si termina

        # valMinimo = selAleatoria  - si termina
        # valMinimo = selMejorFit   - si termina
        # valMinimo = selImpar      - no termina

        # porcentaje = aleatoria    - no termina
        # porcentaje = selMejorFit  - si termina
        # porcentaje = selImpar     - no termina



    def ejecutar(self):
        print("\n")
        print("****************************************************")
        print("**********      Algoritmo corriendo       **********")
        print("****************************************************")

        generacion = 0
        poblacion = self.inicializarPoblacion()
        fin = self.verificarCriterio(poblacion, generacion)

        while(fin == None):
            print("########## generacion: " + str(generacion) + " ##########")
            padres = self.seleccionarPadres(poblacion)
            poblacion = self.emparejar(padres)
            generacion += 1
            fin = self.verificarCriterio(poblacion, generacion)

        # mostrar fin
        self.printPoblacion(poblacion)
        print("*********** GENERACION ", generacion, " ***************")
        
        # obtener el mejor fitness
        ordenDescendente = sorted(poblacion, key=lambda item: item.fitness, reverse=False)
        Singleton.getInstance().modelo = ordenDescendente[0].solucion
        Singleton.getInstance().generacion = generacion
        print("modelo:", Singleton.getInstance().modelo)
        print("")
        print("")


    def printPoblacion(self, poblacion):
        for i in range(len(poblacion)):
            print("~~~~~~~~~~ poblacion[", i, "] ~~~~~~~~~~")
            print("solucion:", poblacion[i].solucion)
            print("fitness:", poblacion[i].fitness)



    """
    *   Función que crea la población
    """
    def inicializarPoblacion(self):
        poblacion = []

        for i in range(self.tamPoblacion):
            solucion = []
            for j in range(self.tamIndividuo):
                solucion.append(self.getRango())
            poblacion.append(Nodo(solucion))

        return poblacion



    def getRango(self):
        return random.uniform(-2, 2)



    """
    *   Función que verifica si el algoritmo ya llegó a su fin
    """
    def verificarCriterio(self, poblacion, generacion):
        result = None

        #actualizar el valor fitness
        for nodo in poblacion:
            nodo.fitness = self.evaluarFitness(nodo.solucion)
        
        if self.criterioFin == 0:
            #maximo numero de generaciones
            if generacion >= self.maxGeneraciones:
                result = True
        
        if self.criterioFin == 1:
            #minimo numero fitness
            for i in range(self.tamPoblacion):
                if poblacion[i].fitness <= self.minFitness:
                    result = True
                    break

        if self.criterioFin == 2:
            #Un porcentaje de la población que tenga un valor fitness igual
            suma_total = 0

            #print(len(poblacion))

            for i in range(len(poblacion)):
                if round(float(poblacion[i].fitness)) <= float(self.espFitness):
                    #print(poblacion[i].fitness, "<=", self.espFitness)
                    suma_total += 1
            #print("")
            #print(self.espPorcentaje)
            #print(self.espFitness)
            #print("")
            #print(suma_total / len(poblacion))
            if (suma_total / len(poblacion)) >= self.espPorcentaje:
                result = True
            
        return result



    """
    *   Función que evalúa qué tan buena es una solución, devuelve el valor fitness de la solución
    *   @solucion = el número viene en un arreglo como este [0, 1, 1, 1, 0]
    """
    def evaluarFitness(self, solucion):
        # Recorrer el numero de entradas
        for i in range(len(self.entrada)):
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
        for i in range(self.tamIndividuo):
            w = solucion[i]
            p = fila[i]
            nc += w * p
        return nc



    def calcularError(self):
        # Recorrer el numero de entradas
        # (x1 - x2) ^ 2
        valor = 0.0
        for i in range(len(self.entrada)):
            fila = self.entrada[i]
            valor += ((fila[4] - fila[5]) ** 2)
        
        return valor / len(self.entrada)



    """
    *   Función que toma a los mejores padres para luego crear una nueva generación
    """
    def seleccionarPadres(self, poblacion):
        mejoresPadres = []

        if self.criterioSel == 0:
            #Selección aleatoria
            mejoresPadres = self.seleccionarPadresAleatoria(poblacion)


        if self.criterioSel == 1:
            #Selección de los padres con mejor valor fitness
            #en este caso el mejor valor fitness son los fitness menores
            mejoresPadres = self.seleccionarPadresMejorFitness(poblacion)

        if self.criterioSel == 2:
            #Selección de padres en posiciones impares o solo en posiciones pares
            mejoresPadres = self.seleccionarPadresImpares(poblacion)

        return mejoresPadres



    def seleccionarPadresAleatoria(self, poblacion):
        mejoresPadres = []
        numGenerados = []
        numRandom = 0

        for i in range(self.noSelPadres):
            while True:
                numRandom = random.randint(0, len(poblacion)) - 1
                find = False

                #revisar si ya existe el individuo como mejor padre
                for num in numGenerados:
                    if numRandom == num:
                        find = True
                        break

                if not find:
                    numGenerados.append(numRandom)
                    break

            #ahora obtener el padre
            mejoresPadres.append(poblacion[numRandom])

        return mejoresPadres



    def seleccionarPadresMejorFitness(self, poblacion):
        mejoresPadres = []

        ordenDescendente = sorted(poblacion, key= lambda item: item.fitness, reverse=False)
        
        for i in range(self.noSelPadres):
            mejoresPadres.append(ordenDescendente[i])

        return mejoresPadres


    
    def seleccionarPadresImpares(self, poblacion):
        mejoresPadres = []
        cont = 0

        for i in range(len(poblacion)):
            if (i % 2) != 0:
                mejoresPadres.append(poblacion[i])
                cont += 1

            if cont == self.noSelPadres:
                break

        return mejoresPadres



    """
    *   Función que toma a los mejores padres y genera nuevos hijos
    """
    def emparejar(self, padres):
        nuevaPoblacion = padres

        #obtener el num de nodos restantes
        noFalta = self.tamPoblacion - self.noSelPadres

        #generar hijos en lo que falte
        for i in range(noFalta):
            numRandom1 = 0
            numRandom2 = 0

            while numRandom1 == numRandom2:
                numRandom1 = random.randint(0, len(padres)) - 1
                numRandom2 = random.randint(0, len(padres)) - 1
            
            padre1 = padres[numRandom1]
            padre2 = padres[numRandom2]

            hijo = Nodo()
            hijo.solucion = self.cruzar(padre1.solucion, padre2.solucion)
            hijo.solucion = self.mutar(hijo.solucion)
            nuevaPoblacion.append(hijo)

        return nuevaPoblacion



    """
    *   Función que toma dos soluciones padres y las une para formar una nueva solución hijo
    """
    def cruzar(self, padre1, padre2):
        hijo = []

        for i in range(self.tamIndividuo):
            numRandom = random.uniform(0, 1)
            if numRandom <= 0.6:
                hijo.append(padre1[i])
            else:
                hijo.append(padre2[i])
        
        return hijo



    """
    *   Función que toma una solución y realiza la mutación
    """
    def mutar(self, solucion):
        nsolucion = solucion

        # 0 mutar   1 no mutar
        numRandom = random.randint(0, 1)
        if numRandom == 0:
            for i in range(self.tamIndividuo):
                numRandom = random.randint(0, 1)
                if numRandom == 0:
                    solucion[i] = self.getRango()

        return nsolucion
