
# POr referencia ---- >   Lista [1,2,3] --------->    Direccion en memoria : 0x45FA001
# TIpos de datos compuestos:  [], {}, ()


def potencia_numeros_naturales(lista_elementos):
    #lista_auxiliar = []                      #  Referencia nueva a una lista 0x454545FA
    for index, dato in enumerate(lista_elementos):
        lista_elementos[index] = dato**2
    
    return lista_elementos

lista_original = [1,2,3,4,5,6,7,8,9]


print(f"Lista Original : {lista_original}")
lista_modificada = potencia_numeros_naturales(lista_original)
print(f"Lista Modificada : {lista_modificada}")
print(f"Lista Original  : {lista_original}")
