



# Diccionarios
diccionario1 = {'1':'True', '2':2.5, '3':3.5, '4':4.5}

def multiplicacion(**kwargs):
    
    multiplicacion = 1
    
    print(f" tipo : {type(kwargs)}")
    
    for key, valor in kwargs.items():      #     index, dato   <---enumerate(lista)
        print(f"{key} : {valor}") 
        multiplicacion *= valor       
    
    print(multiplicacion)    


multiplicacion(n1=1, n2=2, numero=3, valor=4)