#Operadores Comparacion para cadenas

cadena_1 = "Hola2"
cadena_2 = "Hola"

print(cadena_1 == cadena_2) # Operador de comparacion de igualdad '=='
print(cadena_1 != cadena_2) # Operador de comparacion de igualdad '!='

print(cadena_1 > cadena_2) # Operador de comparacion de igualdad '>'
print(cadena_1 < cadena_2) # Operador de comparacion de igualdad '<'
print(cadena_1 >= cadena_2) # Operador de comparacion de igualdad '>='
print(cadena_1 <= cadena_2) # Operador de comparacion de igualdad '<='

print("Comparacion a nivel de longitud")
print (len(cadena_1) == len(cadena_2) )
print (len(cadena_1) > len(cadena_2) )
print (len(cadena_1) < len(cadena_2) )


# Slicing de cadenas

print("*****************************  Slicing ******************************")

#                   012345678910 
cadena_principal = "PYTHON 2024"

print(cadena_principal[0:5])
print(cadena_principal[4:])
print(cadena_principal[:8])
print(cadena_principal[4:9])

#Subcadenas con indices negativos

print("*****************************  Slicing Negativos ******************************")

#                             
cadena_principal = "PYTHON 2024"
print(cadena_principal[:-2])
print(cadena_principal[5:-1])
print(cadena_principal[-1:-1])
print("----")
print(cadena_principal[-1:5])



print("*****************************  Slicing con 3 indices ******************************")

#                   012345678910 
cadena_principal = "PYTHON 2024"
                #   P T O   0 4 

print(cadena_principal[::2])
print(cadena_principal[1::3])
print(cadena_principal[1::3])

























