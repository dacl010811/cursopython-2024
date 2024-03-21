# Operaciones con Archivos en python

from os import *
from paramiko import Channel, ChannelFile
from trace import Trace, _Ignore
from pickle import Pickler

# Importacion de tipo alias
import os.path  as darwin

# Importacion principal para trabajar con ficheros en python
from io import open
from os import path
import time

def crear_archivo_inicial(nombre="Inicio.txt"):
    
    """Crea un archivo vacio, de cualquier extensiòn.
    """    
    
    fichero  = open(nombre,"w")
    fichero.close()
    
    
def llenar_fichero(nombre_fichero,datos,sep="\n"):
        
    fichero = open(nombre_fichero,'w')
    for dato in datos:        
        fichero.write(dato+sep)
    
    fichero.close()
    
    
def leer_fichero_read(nombre_fichero):
    fichero = open(nombre_archivo,"r")
    print(f"********Inicio del contenido del fichero********")
    
    print(fichero.read())
    
    print(f"********Fin del contenido del fichero********")
    fichero.close()
    

def leer_fichero_readline(nombre_fichero):
    fichero = open(nombre_archivo,"r")
    print(f"********Inicio del contenido del fichero********")    
    print(f"{fichero.readline()}")        
    print(f"********Fin del contenido del fichero********")
    fichero.close()
    

def leer_fichero_readlines(nombre_fichero):
    fichero = open(nombre_archivo,"r")
    print(f"********Inicio del contenido del fichero********")
    
    for linea in fichero.readlines():
        print(f"{linea}")
        time.sleep(0.25)
    
    print(f"********Fin del contenido del fichero********")
    fichero.close()
    
# Invocaciones a funciones    

crear_archivo_inicial()
crear_archivo_inicial(nombre="NombreFichero.xls")
crear_archivo_inicial(nombre="NombreFichero.doc")
crear_archivo_inicial(nombre="NombreFichero.pdf")
crear_archivo_inicial(nombre="NombreFichero.bin")
crear_archivo_inicial(nombre="NombreFichero.zip")
crear_archivo_inicial(nombre="NombreFichero.rar")

# Crear fichero  anotaciones.txt
nombre_archivo = 'anotaciones.txt'
#crear_archivo_inicial(nombre_archivo)
#llenar_fichero(nombre_archivo,['Hola','Mundo','Desde','Ficheros en Python'])

# Lectura de un fichero por metodo read()
#leer_fichero_read(nombre_archivo)


# Lectura de un fichero por metodo read()
leer_fichero_readlines(nombre_archivo)











