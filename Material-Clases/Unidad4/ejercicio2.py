

# Invocacion por nombre de variable

def suma(numero_1, numero_2, numero_3):       # Definicion de los parametros de la funcion
    return numero_1 + numero_2 + numero_3

def resta(numero_1, numero_2):
    return  numero_1 - numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2

def division(dividendo, divisor):
    return dividendo / divisor


# Invocacion por nombre de variable
#  No existe un orden de envio de valores

print(f"El resultado de la suma es =  {suma(numero_2=25, numero_3=25, numero_1=10)}")
print(f"El resultado de la suma es =  {suma(numero_1=25, numero_2=25, numero_3=25)}")

print(f"El resultado de la resta es =  {resta(numero_2=500, numero_1=260)}")
print(f"El resultado de la resta es =  {resta(numero_1=1000, numero_2=350)}")



