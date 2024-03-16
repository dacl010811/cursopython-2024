


#Varaible global

valor_extra = 15       # Referencia memoria 0x4fA


def suma(num1, num2):  
    global valor_extra     # Referencia memoria 0x4fA
    valor_extra += 250     
    return  num1 + num2 + valor_extra


# Invocaciones

print(f" La variable global origal es : {valor_extra}")
print(f"La suma = {suma(100, 300)}")
print(f" La variable global final es : {valor_extra}")
