


#Listas en python
# Como represento :   '[]'

lista_1  = [1,2,3,4,5,6,7,8,9]
print(type(lista_1))
print(lista_1)

lista_2  = ['Hola',2,3.5,True,None,[1,2,3,4,5,6,7,8,]]
print(type(lista_2))
print(lista_2)

#Como acceder a los elementos de las listas
          #0 1 2 3 4 5 6 ................ indices
lista_1 = [1,2,3,4,5,6,7]
print(lista_1)

# Instruccion es para obtener   elementos de las listas mediante un indice
print(lista_1[4])

# Cambiar o actualizar el valor de un elemento de la lista
lista_1[0] = '111'
print(lista_1)

lista_1[6] = [True,False,False,False,False,False,False,False,]
print(lista_1)

# Metodo que se utiliza para dterminar # de elementos de la lista

print(f" La lista tiene {len(lista_1)} elementos!!")

# Metodos de Listas

lista_1.append([.2,0.03])
lista_1.append('Quito')
lista_1.append(True)

print(" Elminiar elementos de la lista con el metodo pop")

print(lista_1)
print(lista_1.pop())
print(lista_1)
print(lista_1.pop())
print(lista_1)
print(lista_1.pop())
print(lista_1)
print(lista_1.pop())
print(lista_1)

#  metodo index

print("Metodo Index")
          #0 1 2 3 4 5 6   7
lista_1 = [12,2,1,3,4,5,6,7]
print(lista_1.index(4))

# metodo  Sort

print("Metodo Sort, ordenando elementos")
lista_1.sort()
print(lista_1)

lista_1.sort(reverse=True)
print(lista_1)

#
print("Insertar elementos")
lista_1.insert(1000,'125')
print(lista_1)

# Limpiar  el objeto lista

lista_1.clear()
print(lista_1)

# 
lista_1 = ['1','2']
lista_aux = lista_1.copy()

print(lista_1)

lista_aux.append('333')
print(lista_aux)

# Operaciones  concatenar (+)  y tambien clonar

lista_1 = ['1','2','3','4']
lista_2 = ['11','22','33','44']

lista_final = lista_1 + lista_2

print(type(lista_final))
print(lista_final)


# representar listas sobre listas

lista_a = ['1','2',]
lista_b = ['3','4']
lista_c = ['5','6']
lista_d = ['7']

lista_final  = [ lista_a, lista_b, lista_c,lista_d]
print(lista_final)
print(lista_final[2][1]) #  lista_final[2] --> ['5', '6']
print(lista_final[3][10])











































