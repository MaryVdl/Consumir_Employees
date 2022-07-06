'''
Created on 5 jul. 2022

@author: marisol.vidal
'''
from Employee.add_metodos import crearLista, datas
def opcionEjercicio():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Elige un a opcion: "))
            print(" ")
            correcto = True
        except ValueError:
            print("ERROR, Elige una opcion valida")
    return num
    
def menu():
    salir = False
    opcion = 0
    while not salir:
        print("\n -----------Menu de opciones-----------\n")
        print ("1. Add Datos")
        print ("2. Salir \n")
        opcion = opcionEjercicio()
        if opcion == 1:
            datos = crearLista()
            datas(datos)
        elif opcion == 2:
            print(" ADIOS ".center(80, "-"))
            salir = True
            
menu()        
