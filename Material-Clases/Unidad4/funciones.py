



# Como definir una fucnion

# Funcion sin parametros
def saludo():   
    print("Hola mundo desde una funciòn sin argumentos")

# Funcion con parametros

def saludo_nombre(my_nombre):   
    print(f"Hola como estas : {my_nombre}")

def resta(num1, num2):
    return  num1 - num2


# Invocaciones

saludo() # Sin argumentos 

saludo_nombre("Darwin Calle")   #  Una invocacion con argumentos : Invocacion por posicion
saludo_nombre(my_nombre="Nicolas Calle")   #  Una invocacion con argumentos . Invocacion por nombre

# Una funcion que retorne datos
# palabra reservada "return"

def  suma(numero_1,numero_2):
    return numero_1 + numero_2

# Invocar la funcion suma

resultado = suma(10.2,62)
print(f"El resultado de la funcion suma = {resultado}")

print("Aprendiendo funciones en python")

print(f"El resultado de la funcion resta = {resta(8,5)}")  # Invocacion por posicion

print(f"El resultado de la funcion resta = {resta(num1=80,num2=50)}") # Invocacion por nombre de variable

print(f"El resultado de la funcion resta = {resta(num2=200, num1=180)}") # Invocacion por nombre de variable


# Sumar enteros y floats
print("***************************")

print(f"El resultado de la funcion suma = {suma(10.20, 0.62):.2f}")







