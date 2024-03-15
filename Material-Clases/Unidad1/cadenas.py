

#Representacion  de Strings

cadena_1 = "Hola"
cadena_2 = 'Mundo'
cadena_3 = """
           Este 
             es un
             Ejemplo de Cadenas multiples \n
             darwin \t calle
             \r code            
           """
           
print(type(cadena_1))
print(type(cadena_2))
print(type(cadena_3))

print(f"")
print(cadena_2)
print(cadena_3)

#Signo para concatenar cadenas va es signo (+)

cadena_a =  "Darwin "
cadena_b =  "Python "
cadena_c =  "Hola Mundo"

cadena_final = cadena_a + cadena_b + cadena_c
print(cadena_final)

print(f"El resultado de concatenar: {cadena_a}, {cadena_b}, {cadena_c} es  = {cadena_final}")

#Caracter para escapar simbolos dentro de cadenas
# '\'
# I`am Monty Python

print("I`am \"Monty Python\"")
print('I`am "Monty2 Python"')

# Cadena Vacia o Nulas

cadena_nula = ''
cadena_nula = ""
cadena_nula = None  #  Es utilizar esta forma

#Operaciones con Cadenas

# Operacion 1 : Concatenar  (+)
# Operacion 2 : Multiplicar (*)

cadena_1 = "Hola Mundo "
cadena_2 = "Python 3 "

print(cadena_1 + cadena_2)
print(cadena_1*10)
print(cadena_2*5)

#Metodos de Cadenas

print(type(cadena_1))

print("*********************  Metodos de la clase String ***************************")
cadena_1 = "Hola Mundo"
print(cadena_1.upper())

cadena_1 = "hola mundo desde python"
print(cadena_1.capitalize())

cadena_1 = "hola mundo desde python"
print(cadena_1.replace('o','X').upper())

cadena_x = "Hola "
print(cadena_x.join(['x','y','z']))

#           012345678910
cadena_x = " Hola mundo"   # Lista de caracteres: ['H','o','l','a'....]
print(cadena_x.index('mundo'))

cadena_x = "333"
print(cadena_x.isalnum())

print("----- -----")
cadena_x = '0123456789###'	
print(cadena_x.isdigit())

# Validaciones en cadenas 
# Operador in

cadena_1 = "holax"
cadena_2 = "hola mundo holax"

print("Validaciones de Cadenas")
print(cadena_1 not in cadena_2)






























