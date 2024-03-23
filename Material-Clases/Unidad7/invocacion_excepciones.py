




def my_saludo(mensaje):
    try:
        if  not mensaje:
            #print("Error: no se permiten nulos.")
            raise ValueError("Error: no se permiten nulos.")
    except ValueError as e:
        print("Error: no se permiten nulos desde el bloque except!!")
    
    print(mensaje)


my_saludo(None)


def edad():
    try:
        edad = -10
        if edad < 0:
            raise ValueError("La edad no puede ser negativo!!")        
    except ValueError as ve:
        print("Error:",ve)

edad()
