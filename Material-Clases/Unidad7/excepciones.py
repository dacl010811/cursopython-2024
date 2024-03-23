




        #0 1 2
lista = [1,2,3]
num_1 = 100
num2 = 0

try:
    
    for e in lista:
        lista.pop(1)   
     
    print(lista)
        
    division =  num_1 / num2
    
#except :
#    print("Ha ocurrido un error!!")
except ZeroDivisionError as zde:
    print(f"Error de Division por Cero : {type(zde).__name__}")
except IndexError as ie:
    print(f"Error de Index : {type(ie).__name__}")
except Exception as e:
    print(f"Ha ocurrido un error general!! : {type(e).__name__}")
else:
    print("Ingresa al else si todo fue controlado adecuadamente!!!")
finally:
    print("Ocurra lo q ocurra en el bloque try, siempre pasara por aqui")   
     
    


    


