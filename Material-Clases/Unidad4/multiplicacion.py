
import time   # Importando modulos de python
import os

def generar_tablas_multiplicar(numero_tabla):
        
    for num in range(1,13):
        print(f"{numero_tabla} * {num} = {numero_tabla * num}")
        time.sleep(0.15)
        
        

def generar_tablas_multiplicar_defecto(numero_tabla,limite_tabla=12):
        
    for num in range(1,limite_tabla+1):
        print(f"{numero_tabla} * {num} = {numero_tabla * num}")
        time.sleep(0.15)


menu = """
       ****************************************************
       *        MENU PRINCIPAL DE LA APLICACION           * 
       **************************************************** 
       
       Elija la opciòn del reto que desea ejecutar:
       1 :  Tablas de Multiplicar
       1001 :  Suma Simple
       1002 :  Area Criculo
       1003 :  Suma 2 numeros
       1004 :  Multiplicacion 2 numeros
       1005 :       
       1037 :   Ejemplo 
       0 :   Salir programa  
"""
bandera = True

while bandera:
    print(menu)
    respuesta_usuario = int(input("Ingrese una opcion del menu para ejecutar: \n"))
    if respuesta_usuario == 0:
        break
    elif respuesta_usuario == 1:
        num_tabla =  int (input("Ingresa el numero de la tabla que deseas generar: \n"))
        limite_tabla = int (input("Ingresa el limite de la secuencia de la tabla \n"))
        if limite_tabla > 0:        
            generar_tablas_multiplicar_defecto(num_tabla,limite_tabla)
        time.sleep(2) 
        os.system("cls")    
    else:
        print("La opcion seleccionada no existe!!")

