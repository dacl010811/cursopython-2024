



# Argumentos Indeterminados pero con diccionarios

# Incova la funcion va a enviar una estructura de datos de tipo diccionario

def  concatenar_cadenas(**kwargs):   
    cadena_final = ''
    cadena_final_1 = ''
    
    for key in kwargs:
        #print(f"key = {key} - dato = {kwargs[key]}")
        cadena_final += kwargs[key] + ' '
    
    for k, v in kwargs.items():
        #print(f"{k} --- {v}")
        cadena_final_1 += v + ' '
    
    
    return cadena_final, cadena_final_1

#Invocacion de la funcion

print(f"La cadena final es: {concatenar_cadenas(c1='Hola', c2='Mundo', c3='en', c4='Python')}")

print(f"La cadena final es: {concatenar_cadenas(c1='Hola', c2='Mundo')}")

print(f"La cadena final es: {concatenar_cadenas( c2='Mundo', c4='Python')}")

print(f"La cadena final es: {concatenar_cadenas(c3='en', c4='Python')}")



