




# Tuplas son inmutables
tupla_1 = (1,2,3,4,5,6,7,8,9,10)  #  *args
#tupla_1 [0] = 100
print(f"La tupla tiene {tupla_1}")

def triplica(*args):
    for i in args:
        pass

#triplica(1,3,2)
#triplica(tupla_1)


# Dicionarios:

dicionario_1 = {'1':100, '2':200, '3':300, '4':400, 'A': 'LibroA'}

for k in dicionario_1.keys():
    print(f"key : {k}")

for v in dicionario_1.values():
    print(f"Valor : {v}")
    
    
for k,v in dicionario_1.items():
    print(f"{k} <--> {v}")
    
    
    
    











