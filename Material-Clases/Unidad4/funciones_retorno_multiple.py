





def  presenta_serie_datos():
    lista = []
    my_tupla = ('a','b','c')   # Estructuras inmutables
    
    for e in range(1,21):
        lista.append(e)         
        
    return lista, my_tupla     #  retornamos una lista --->   Resultado final siempre sera una tupla (lista, my_tupla)


#print(f"La lista de datos es: \n {presenta_serie_datos()}")

resultado_tupla = presenta_serie_datos()
print(f"Tipo: {type(resultado_tupla)}")
print(f"DATOS: {resultado_tupla}")

lista_resultado, tupla_resultado = presenta_serie_datos()

print(f"lista_resultado: {lista_resultado}")
print(f"tupla_resultado: {tupla_resultado}")



