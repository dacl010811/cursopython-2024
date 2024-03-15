

# Definicion de funcion 
def  multipliacacion(num1,num2,num3,num4):   # Parametros
    return num1 * num2 * num3 * num4

print(f" El resultado de la multipliacion es = {multipliacacion(5,3,2,3)}") # Invocacion por posicion 

print(f" El resultado de la multipliacion es = {multipliacacion(num3=5,num4=3,num2=2,num1=3)}") # Invocacion por nombre de variable

print(f" El resultado de la multipliacion es = {multipliacacion(num4=5,num3=3,num2=2,num1=3)}") # Invocacion por nombre de variable



