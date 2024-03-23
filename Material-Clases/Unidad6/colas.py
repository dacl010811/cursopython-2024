





#Colas
# Añadir elementos
# Quitar elementos
# Primero en Entrar es el primero en salir (FIFO)

import json  # Importacion de un modulo completo
import collections # Importacion de modulo completo

from collections import deque   #  IMportacion bajo demanda

cola = deque() # Ya creo una cola vacia
print(f" Objeto : {cola}")
print(f" Tipo : {type(cola)}")

cola_1 = deque(['Darwin','Python','2024']) # Ya creo una cola vacia
print(f" Objeto : {cola_1}")
print(f" Tipo : {type(cola_1)}")

#Acciones en las colas
cola.append("Loja")
cola.append("Ecuador")
cola.append("2024")

print(f"La cola tienes : {cola}")

# Simular  First Out
cola.popleft()
print(f"La cola tienes : {cola}")

def suma():
    if len(cola):
        if len(cola):
            if len(cola):
                pass
    else:
        pass

print(f"{suma(4,5)}")


