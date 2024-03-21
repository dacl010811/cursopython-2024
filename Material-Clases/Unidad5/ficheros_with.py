



# Forma moderna de  gestionar ficheros
# Python manejo de forma adecuada el flujo de la informacion sobre los archivos
# with

def crear_fichero_with(nombre_fichero='Fichero_texto.txt'):
    """Crear un fichero, con la instruccion 'with', dandole la gestiòn y control a python

    Args:
        nombre_fichero (str, optional): _description_. Defaults to 'Fichero_texto.txt'.
    """    
    with open(nombre_fichero,'w') as f:
        print(f"tipo dato : {type(f)}")
        print(f"Se creo con exito!!")
        

def leer_fichero_with(nombre_fichero):
    with open(nombre_fichero,"r") as f:
        import time
        for linea in f.readlines():
            print(linea)
            time.sleep(0.25)
            

def llenar_fichero_with(nombre_fichero, datos, sep="\n"):
    with open(nombre_fichero,"w") as f:        
        for dato in datos:
            f.write(dato+sep)

crear_fichero_with(nombre_fichero="Curso.txt")
llenar_fichero_with("Curso.txt",['Darwin', 'Calle', 'Python','Darwin', 'Calle', 'Python','Darwin', 'Calle', 'Python','Darwin', 'Calle', 'Python'])
leer_fichero_with(nombre_fichero="Curso.txt")
