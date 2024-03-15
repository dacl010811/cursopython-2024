

#Operadores :
#   a += 1  --->    a =  a + 1
#   a -= 1  --->    a = a - 1
#   a *= 1  --->    a = a * 1
#   a /= 1  --->    a = a / 1
#   a %= 2  --->    a = a % 2
#   a //= 2 --->    a = a // 2
#   a **= 2 --->    a = a ** 2

contador = 1
while  contador <= 10:
    print(f"Secuencial: {contador}")   
    contador += 1
    if contador == 6:
        break 
else: 
    print(f" El while se ejecuto correctamente, sin novedades")
    


print("Estasmos practicando  CONTINUE")

contador = 1
while  contador <= 10:          
    print(f"Secuencial: {contador}") 
    contador += 1
    if contador == 6:
        continue        
else: 
    print(f" El while se ejecuto correctamente, sin novedades")