#Menú principal
import time
import grafo as g

def escogerOpcion():
    print("-----------------------------------------")
    print("1. Encontrar la ruta más corta entre dos vertices de un gráfo")
    print("0. Salir del programa")
    opcion = int(input("Escoja una opción:"))
    return opcion


def activarOpcion():
    salir= False
    opcionMenu = escogerOpcion()
    while not salir:
        try:
            if(opcionMenu == 1):
                g.rutaMasCorta()
                activarOpcion()
                break
            elif(opcionMenu == 0):
                fin()
                salir = True
                break
            else:
                print("-----------------------------------------")
                print("¡Por favor digita una opción correcta!")
                activarOpcion()
                break
        except:
            print("Opción incorrecta")
    

#Salir del programa
def fin():
    print("¡Gracias por haber usado nuestro programa!")
    time.sleep(2)
    print("Cerrando programa en:")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)