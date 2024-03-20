



def concatenar_n_cadenas(*args,separator='_'):
    cadena_final = ''
    for arg in args:
        cadena_final += arg + separator
    return cadena_final

#Invocacion por  tuplas ---->  *args

print(f"Cadena final : {concatenar_n_cadenas('Estoy','en','Quito','Ecuador','Abacom','Linux','Mac',separator='#')}")


#Promedio de notas

def promedio_notas(*args):
    
    """Calcula el promedio de las notas de un alumno

    Returns:
        promedio_notas_final: Representa la nota final del alumno
    """    
    
    promedio_notas_final = 0.0    
    for arg in args:
        promedio_notas_final += arg

    return promedio_notas_final / len(args)

print(" Promedio de Notas")
print(f" El promedio final = {promedio_notas(400,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5,10,5):.2f}")

# {'k': valor}

# Crear un diccionario mediante el envio de argumentos clave=valor

def devolver_diccionario(**kwargs):
    
    """Devuelve un objeto de tipo diccionario,  en base a los argumentos enviados

    Returns:
        kwargs: Representa un diccionario de datos
    """    
    
    return kwargs

print()
print()

print(f" dic = {devolver_diccionario(num1=5.2,bandera=True,my_lista=[1,2,3],entero=10,my_tupla=(1,2,3),my_diccionario={'1':'A'})}")
print(f" dic = {devolver_diccionario(num1=5.2,bandera=True,my_lista=[1,2,3],entero=10,my_tupla=(1,2,3),my_diccionario={'1':'A'})['my_tupla']}")


# *args  ---> (True, 5.2, 1, 2 , 10 , 45, 78.8, 46) ---->  Repuesta :  (2,10,46)
# if num % 2 == 0  --> Numero par

def obtener_numeros_pares():
    pass


# cadena.upper()


def  convertir_a_mayusculas(*args):
    
    """Convierte cadena a MAYUSCULAS

    Returns:
        Lista: Representa el resultado de la conversion.
    """    
    
    lista_final = []
    for arg in args:
        lista_final.append(arg.upper())        
    return lista_final

print(f" La conversion = {convertir_a_mayusculas('HOla','munDO','PYthon','2024')}")

 
