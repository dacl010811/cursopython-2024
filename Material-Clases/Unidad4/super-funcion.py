


# Super funcion, se conforman de argumentos indetterminados
# de tipo  *args y **kwargs


#def  suma(num1, num2, num3, num4):
#    pass
# Invocacion de suma, por posicion
#suma(1,5,6,8)

#def  multiplicacion(valor1, valor2, valor3):
#    pass
#Incocacion de multiplicacion, vamos a realizar por nombre de variable
#multiplicacion(valor3=8, valor1=7, valor2=2)

# El orden simepre va a ser el siguiente :

# 1.- Enviamos los datos por posicion --->   1,2,3,4
# 2.- Enviamos los datos por nombre  porterior al  punto 1


def super_funcion_suma(*args, **kwargs):  #  1,2,3,4, num1=5, num2=10, num3=15
    
    """Esta super funcion suma n numeros, mediante tuplas y diccionarios

    Returns:
        suma_total: float
    """    
        
    suma_total = 0        
    for arg in args:        
        print(f"{arg}")
        suma_total += arg
                
    for k in kwargs:
        print(f"{kwargs[k]}")
        suma_total += kwargs[k]
        
    return suma_total
        
print(f"La suma total: {super_funcion_suma(20,20,20,100,5,2,3,5.2,.02,num1=10,num2=20,num3=30, num4=.8):.1f}")

