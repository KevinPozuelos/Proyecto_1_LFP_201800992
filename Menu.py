from AutomataMenu import *
from funtion import *
entrada = automataMenu()
def menu():

    print("Proyecto 1")
    print("-----------------")
    print("1.- Cargar Menu")
    print("2.- Cargar Orden")
    print("3.- Generar Menu")
    print("4.- Generar Factura")
    print("5.- Generar arbol")
    print("6.- Salir")
    opcion = input('>>Ingrese una opcion: ')
    return opcion


def menuP():

    while True:
        opcion = menu()
        if opcion == '1':
            cadena = openFile()
            entrada.analizador(cadena)

        # elif opcion == '2':

        # if opcion == '3':

        # if opcion == '4':

        # elif opcion == '5':

        if opcion == '6':
            break



