

# Encriptar la informacion
import pickle

datos = [1,2,3,4,5,6,7,8,9,10]

def  crear_archivo(nombre_archivo,ext=".bin"):
    fichero = open("".join([nombre_archivo,ext]) , "wb")          
    fichero.close()


def guardar_informacion(nombre_archivo,datos):
    fichero = open(nombre_archivo, "wb")
    pickle.dump(datos, fichero)
    fichero.close()
    
def leer_archivo_binario(nombre_archivo):
    fichero = open(nombre_archivo, "rb")
    datos = pickle.load(fichero)    
    print("La informacion desencriptada es : \n")
    print(datos)
    

crear_archivo("CursoPython")
guardar_informacion("CursoPython.bin",{'0':'A', '1':'B', '2':'C', '3':'D','4':'DD','5':'XY'})
leer_archivo_binario("CursoPython.bin")
