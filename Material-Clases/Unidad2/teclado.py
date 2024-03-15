


# Ingreso de datos por teclado
#  funcion principal es :   'input()'
#  funcion print me sirve para mostar informacion en pantalla

valor_ingresado =  input("Cual es tu nombre > \n")

print(type(valor_ingresado))
print(f" El nombre ingresado es : {valor_ingresado}")


# Funciones que se utilizan para las conversiones  de datos
# int()  --->   Convierte un str >>>>   int
# float() --->  Convierte un str >>>> float    
# bool() ---> Convierte un str >>>> bool
# str() ---> Convierte un str 

constante = 10
edad = int( input("Ingresa tu edad: \n") )
print(edad + constante)

#Conversiones a  flotantes

estatura = float( input("Ingresa tu estatura: \n") )
print(estatura + constante)

# Conversiones a boolean
respuesta = bool( input("Ingresa una respuesta: \n") ) #  True, False, 0 ----> False  y  1 ---- True
print(respuesta)

respuesta = bool('True')
print(respuesta)

# Conversiones a str()

print ("----- Conversiones a Cadenas o Strings")
variable_12 = 1000
print(type(variable_12))

print(type(str(variable_12)))



def hola():
    pass















