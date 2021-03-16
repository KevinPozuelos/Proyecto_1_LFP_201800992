from AutomataMenu import *
from funtion import *
from AutomataFactura import *
entrada = automataMenu()
entrada2 = AutomataFactura()
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
            contador = 1
            cadena = openFile()
            listatk = entrada.analizador(cadena)
            for i in listatk:
                print(str(contador),' : ', i)
                contador += 1

        elif opcion == '2':
            factura = openFile()
            entrada2.analizadorF(factura)
        # if opcion == '3':

        # if opcion == '4':

        # elif opcion == '5':

        if opcion == '6':
            break



