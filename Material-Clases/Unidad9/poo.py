



#print(type("").__name__)

class Animal():   # Considerar como una plantilla o mode
    
    #Atributos de una clase
    edad = 0
    genero = ''
    
    #Metodos
           
    def __init__(self, nombre, edad, genero):  # Constructor 
        #Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        
    def __str__(self) -> str:
        return "Clase : [Nombre:{0} - Edad:{1} - Genero:{2} ]".format(self.nombre,self.edad,self.genero)
        
    # Metodos de Instancia
    def comer(self):
        print (f"Estoy alimentandome!!: {self.nombre}")
    
    def dormir(self):
        print (f"Estoy durmiendo!!: {self.nombre}")
    
    def correr(self):
        print (f"Estoy corriendo!! : {self.nombre}")
    

# Instanciar una clase :  Simplemente es sacar una copia
# Crear objetos :   Simplemente es sacar una copia mediante la plantilla denominada "Clase"

perro = Animal("Perro",5,'macho')   # Invocacion al constructor de la clase
print(type(perro))
#Acceso a los atributos de instancia
perro.nombre = "Booby"
perro.edad = 115
perro.genero = "hembra"

#Invocacion al metodo  de instancia
perro.correr()
perro.dormir()
perro.comer()

print(perro)

perro_1 = Animal("Perro_1",5.8,'Hembra') 
print(perro_1)


perro_2 = Animal("Perro_2",115,'macho') 
print(perro_2)


perro_3 = Animal("Perro_3",50,'macho') 
print(perro_3)

#gato = Animal()  
#pato = Animal()  
#tortuga = Animal()  






# Heredar un comportamineto:  Herencia y Encapsulamiento
