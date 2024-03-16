

# Concepto de Parametros por defecto
# Simplemente es aquel q tiene un valor incial y cuya varaible de este tipo es opcion el enviar su valor



def suma(numero_1,numero_2,numero_3=15):       # Definicion de los parametros de la funcion
    return numero_1 + numero_2 + numero_3

def resta(numero_1, numero_2, num3=1):
    return  numero_1 - numero_2 - num3

# Invocacion

print(f"El resultado de la suma es =  {suma(10,20,1000)}")

print(f"El resultado de la suma es =  {suma(numero_2=10,numero_1=20, numero_3=1800)}")


