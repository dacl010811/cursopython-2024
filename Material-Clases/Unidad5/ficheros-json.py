



import json

contactos = [("Darwin","Calle","Profesion","dacl010812@gmail.com"),
             ("Jose","Calle","Profesion","dacl010813@gmail.com"),
             ("David","Lopez","Profesion","dacl0108141@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl0108151@gmail.com"),
             ("David","Lopez","Profesion","dacl0108141@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl0108115@gmail.com"),
             ("David","Lopez","Profesion","dacl0108114@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl01081115@gmail.com"),
             ("David","Lopez","Profesion","dacl01011814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl01110815@gmail.com"),
             ("David","Lopez","Profesion","dacl010814@gmail.com"),
             ("Martha","Cisneros","Profesion","dacl010815@gmail.com")
             ]

datos = []

for nombre, apellido, profesion, email in contactos:
    datos.append({'nombre':nombre, 'apellido':apellido, 'profesion':profesion, 'email':email})

with open("archivo.json","w") as filejson:
    json.dump(datos, filejson)
    

#Lectura de Archivos JSON
with open("archivo.json","r") as filejson:
    datos = json.load(filejson)
    print(f"Data: {datos}")
    print(f"Tipo {type(datos)}")
    
    print("************************************")
    print()
    for contacto in datos:
        print(f"{contacto['nombre']} -- {contacto['apellido']} -- {contacto['profesion']} -- {contacto['email']} ")

