class Singleton:
   __instance = None

   nombre         = ""
   entrada        = []
   criterioFin    = 0
   criterioSel    = 0
   generacion     = 0
   modelo         = []

   """
      0 - Maximo numero de generaciones
      1 - Un valor minimo alcanzado por una solucion de la poblacion
      2 - Un porcentaje de la población que tenga un valor fitness igual
   """
   """
      0 - Selección aleatoria
      1 - Selección de los padres con mejor valor fitness
      2 - Selección de padres en posiciones impares o solo en posiciones pares
   """
   def getCriterioFin(self):
      if self.criterioFin == 0:
         return "Max_Num_Generacion"
      elif self.criterioFin == 1:
         return "Val_Minimo_Alcanza"
      else:
         return "Porcentaje_Val_Fit"

   def getCriterioSel(self):
      if self.criterioSel == 0:
         return "Sel_Aleatoria"
      elif self.criterioSel == 1:
         return "Sel_Mejor_Fit"
      else:
         return "Sel_Impar_Fit"

   @staticmethod 
   def getInstance():
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self
