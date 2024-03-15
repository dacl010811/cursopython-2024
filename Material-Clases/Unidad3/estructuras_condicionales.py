


# Estructura if

numero_1 = 10
numero_2 = 20


if  numero_1 >= numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")

if  numero_1 < numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")

if  numero_1 > numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")

if  numero_1 != numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")

if  numero_1 == numero_2:
    print(f" El numero 1 es mayor que el 2 : {numero_1}")
    
    
# if -else

if numero_1 > 0: # Condicion es verdadera 
    print("Condicion verdadera")
else:
    print("Condicion es falsa")
    
# if - elif -else

numero_1 = -1 
numero_2 = -1 

if numero_1 < 0:
    print("a")
elif numero_2 > 10:
    print("b")
elif numero_2 != 10:
    print("c")
elif numero_2 > 100:
    print("b")
    if numero_2 != -2:
        print("XXXXXXX")
        if numero_1 != -1:
            print('Hola1')
        else:
            print('Hola2')
else:
    print("Ruta por defecto!!")



if numero_1 < 0:
    print("a")
elif numero_2 > 10:
    print("c")
elif numero_2 > 101:
    print("c")
elif numero_2 > 102:
    print("c")
else:
    print("Valor nulo")


# 

producto_1 = "12 1 5.30"
producto_2 = "16 2 5.10"

valores =  producto_1.split(" ")

print(type(valores))
print(valores)