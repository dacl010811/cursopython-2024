


# Estructuras de Control

menu = """
       ****************************************************
       *        MENU PRINCIPAL DE LA APLICACION           * 
       **************************************************** 
       
       Elija la opciòn del reto que desea ejecutar:
       1000 :  Hello Mundo
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
    opcion = int (input("Elija una opción: \n"))
    if opcion == 0:
        print("Hasta pronto!!")
        break
    elif opcion == 1000:
        #Ejercicio 1000
        print("Hello World!") 
    elif opcion == 1001:
        # Ejercicio 1001
        A = int(input("Ingrese #1 de la suma : \n"))
        B = int(input("Ingrese #2 de la suma : \n"))
        X = A + B
        print(f"X = {X}")
    elif opcion == 1002:
        # Ejercicio 1002
        pi = 3.14159
        radio = float(input("Ingrese el radio de la circunferencia: \n"))
        area = pi * radio**2

        print(f"A={area:.4f}")
    else:
        print("La opcion seleccionado no existe!!!")
    







