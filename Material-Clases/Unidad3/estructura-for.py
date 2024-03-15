


lista = [1,2,3,4,5,6,7,8,9,10,11]
tupla_1 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

for e in tupla_1:    
    if e == 1:
        break
    else:
        print(f"E: [{e}]")
else:
    print("Ejecucion satisfactoria!!")
    
    
# Clase enumerate()
     #   0  1  2  3  4  5  6  7  8  9   10   --->>>  Indices de los elementos de la lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

      #     0    1    2    3    4    5    6    7
tupla_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
           #   indice , valor 
           
for indice,valor in enumerate(tupla_1):
    if indice % 2 == 0:
        print(f"{indice} -> {valor}")




