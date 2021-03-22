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

            cadena = openFile()
            entrada.analizador(cadena)
            entrada.sintaxisError()
            entrada.reporteToken()
            entrada.reporteError()


        elif opcion == '2':
            factura = openFile()
            entrada2.analizadorF(factura)
            entrada2.reporteToken()
            entrada2.reporterror()

        if opcion == '3':

            listaOrdenada = entrada.ordenarSecciones()
            entrada.vista(listaOrdenada)
        if opcion == '4':
            entrada2.vistaFactura()
        elif opcion == '5':
            listaOrdenada = entrada.ordenarSecciones()
            entrada.generarGraph(listaOrdenada)
            
        if opcion == '6':
            break



