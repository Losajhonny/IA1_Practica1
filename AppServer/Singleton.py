class Singleton:
   __instance = None

   entrada        = []
   criterioFin    = 0
   criterioSel    = 0

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
