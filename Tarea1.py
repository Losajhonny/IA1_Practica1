
def init():
    while True:
        print("*******************************")
        print("* 1. Busqueda en profundidad. *")
        print("* 2. Busqueda en amplitud.    *")
        print("* 3. Salir                    *")
        print("*******************************\n")

        numero = int(input("Selecciar opcion: "))
        
        print(numero)

        if numero == 1:
            profundidad()
        elif numero == 2:
            amplitud()
        elif numero == 3:
            break

def profundidad():
    print("Profundida")

def amplitud():
    print("amplitud")

init()