class Singleton:
   __instance = None

   entrada = []
   tamPoblacion = 10
   criterioFin = 0
   entradaFin = 100
   criterioSeleccion = 0
   entradaSeleccion = 10

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

#s = Singleton()
#print (s)

#s = Singleton.getInstance()
#print (s)

#s = Singleton.getInstance()
#print (s)