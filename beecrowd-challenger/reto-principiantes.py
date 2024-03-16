import time
import os
from colored import Fore, Back, Style

def mostrar_menu():

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
    
    return menu

def saludo():
    print("Hola Mundo desde python")
  
  
def limpiar():    
    os.system(command="cls")    

  
if __name__ == "__main__":
    bandera = True
    while bandera:
        print(f"{Fore.yellow}{mostrar_menu()}{Style.reset}")
        opcion = int (input("Elija una opción: \n"))
        if opcion == 0:
            print(f"{Fore.yellow}Hasta pronto!!{Style.reset}")
            time.sleep(2)
            limpiar()
            break
        elif opcion == 1000:
            saludo()
            time.sleep(2)
            limpiar()
        else:
            print(f"{Fore.dark_blue}La opcion seleccionada no existe!!{Style.reset}")
            time.sleep(2)
            limpiar()
            