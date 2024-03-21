

import time

# Operacion Extender ----> append

def crear_fichero_with(nombre_fichero='Fichero_Append.txt'):
    """Crear un fichero, con la instruccion 'with', dandole la gestiòn y control a python

    Args:
        nombre_fichero (str, optional): _description_. Defaults to 'Fichero_texto.txt'.
    """    
    with open(nombre_fichero,'a+') as f:
        print(f"tipo dato : {type(f)}")
        print(f"Se creo con exito!!")
        

def llenar_fichero_append(nombre_fichero="Fichero_Append.txt",sep="\n"):
    fichero = open(nombre_fichero,'a+')
    for linea in range(1,11):
        fichero.write(f"Linea-{linea}{sep}")
        
        
def leer_fichero_append(nombre_fichero="Fichero_Append.txt"):
            
    fichero = open(nombre_fichero,'r')
    for linea in fichero.readlines():
        print(f"{linea}")
        time.sleep(0.15)
            


def modificar_linea_append(nombre_fichero="Fichero_Append.txt"):
    with open(nombre_fichero,'r+') as f:
        lista_lineas = f.readlines()
        for index, linea in enumerate(lista_lineas):
            if index % 2 != 0:
                lista_lineas[index] = "Linea modificada\n"                
        f.seek(0)
        f.writelines(lista_lineas)


crear_fichero_with()
llenar_fichero_append()
leer_fichero_append()
modificar_linea_append()