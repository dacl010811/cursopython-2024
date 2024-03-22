import csv




# Variable global
contactos = [("Darwin","Calle","Profesion","dacl010812@gmail.com"),
             ("Jose","Calle","Profesion","dacl010813@gmail.com"),
             ("David","Lopez","Profesion","dacl010814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl010815@gmail.com"),
             ("David","Lopez","Profesion","dacl010814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl010815@gmail.com"),
             ("David","Lopez","Profesion","dacl010814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl010815@gmail.com"),
             ("David","Lopez","Profesion","dacl010814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl010815@gmail.com"),
             ("David","Lopez","Profesion","dacl010814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl010815@gmail.com")
             ]



def crear_archivo_csv(nombre_archivo):    
    with open(nombre_archivo,"w") as csvfile:
        csvfile.close()
        
def guardar_datos_csv(nombre_archivo,datos):    
    with open(nombre_archivo,"w",newline="\n") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for dato in datos:
            writer.writerow(dato)
            
def leer_datos_csv(nombre_archivo):    
    with open(nombre_archivo,"r",newline="\n") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        print(type(reader))
        print(reader)
        for nombre, apellido, profesion, correo in reader:
            print(nombre, apellido, profesion, correo)
            
        
        
crear_archivo_csv("Datos.csv")
guardar_datos_csv("Datos.csv",contactos)
leer_datos_csv("Datos.csv")
        
        
        


        
        
    

