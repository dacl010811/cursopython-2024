


# Ambito de variables :
# variables globales
# variables locales

valor_local = 1000     # Definicion de una varaible global  x0FA25
bandera = True         #  Variable Global
var_boolean = False

def suma(num_1, num_2):
    var_boolean = True  # Variables locales a la funcion
    valor_local = 400   # Memora ---->  0x254545 
    return  num_1 + num_2

print(f"Suma = {suma(500,250)}")

print(valor_local) 
print(var_boolean)



