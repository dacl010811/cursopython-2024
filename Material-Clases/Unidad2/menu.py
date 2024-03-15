import time
import os

bandera = True

menu = """
        Este es el menu principal de la aplicacion.
        Opciones:
        1.- hola mundo
        2.- suma de 2 numeros
        3.- suma de 3 numeros
        0.- salir
"""
while bandera:
    print(menu)
    respuesta = int(input("Elije una opcion del menu para ejecutar el programa: \n"))
    if respuesta == 0:
        break
    elif respuesta == 1:
        print("Hola mundo!!!")   
        time.sleep(5)     
        os.system("cls")
    elif respuesta == 2:
        numero_1 =  int(input("Ingresa el primer numero : \n"))
        numero_2 =  int(input("Ingresa el segundo numero : \n"))
        
        print("La suma de {} + {} = {}".format(numero_1, numero_2,numero_1+numero_2))
        