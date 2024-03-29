


# UML

class Zoologico():
    
    # Atributos de Clase
    lista_visitantes = []
    lista_zonas = []
    lista_animales = []
    
    #Encapsulamiento
    __ganancias = 10000
    __facturacion_valor = 100000
    
    def __init__(self,nombre,direccion,horario,lista_zonas=[],lista_animales=[]) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.horario = horario
        self.lista_zonas = lista_zonas
        self.lista_animales = lista_animales
        
    def __str__(self) -> str:
        return f"Zoologico: {self.nombre},{self.direccion}"
    
    
    def agregar_zona(self,lista_zonas=[]):
        for zona in lista_zonas:
            self.lista_zonas.append(zona)
    
    def agregar_animal(self,lista_animales=[]):
        for animal in lista_animales:
            self.lista_animales.append(animal)        
                
    def mostrar_ganancias(self):
        return f"El zoloogico: {self.nombre}, ha ganado en el mes: {self.__ganancias}"
    
    def __facturacion(self):  # Encapsulamiento
        return self.__facturacion_valor * 255
    
    def mostrar_facturacion(self):  # Encapsulamiento
        return self.__facturacion()
    
    def mostrar_zonas(self):
        for zona in self.lista_zonas:
            if isinstance(zona,Zona_Zoologico):
                print(f"Zona: {zona.nombre}")
    
    def mostrar_animales(self):
        for animal in self.lista_animales:
            if isinstance(animal,Animal):
                print(f"Animal: {animal.nombre}")
    
            
class Visitante():
    def __init__(self,nombre, apellido,cedula,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
        
    def __str__(self) -> str:
        return f"{Visitante:{self.nombre},{self.apellido},{self.cedula},{self.edad}}"
        

class Zona_Zoologico():
    def __init__(self, nombre, responsable) -> None:
        self.nombre = nombre
        self.responsable = responsable
        
    def __str__(self) -> str:
         return f"{Zona_Zoologico:{self.nombre},{self.responsable}}"
    
class Animal():           # Super clase 
    
    def __init__(self,nombre,edad,especie,color) -> None:
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.color = color
    
    def __str__(self) -> str:
        return f"{Animal:{self.nombre},{self.edad},{self.especie},{self.color}}"
    
    def emitir_sonido():
        pass
       

class Leon(Animal):         # Subclases, o tambien clases derivadas
    
    def __init__(self,nombre,edad,especie,color,genero) -> None:
        #super().__init__(self,nombre,edad,especie,color)
        Animal.__init__(self,nombre,edad,especie,color)
        
        self.genero = genero
    
    def __str__(self) -> str:
         return f"Leon: {Animal.__str__()},{self.genero}"
     
    def emitir_sonido(self) -> None:
         print("!!!Rugido!!")
     
         

class Elefante(Animal):
    def __init__(self,nombre,edad,especie,color) -> None:
        Animal.__init__(self,nombre,edad,especie,color) 
    
    def __str__(self) -> str:
         return f"Elefante: {Animal.__str__()}"
     
    def emitir_sonido(self) -> None:
         print("!!!Barritido!!")

class Serpiente(Animal):
    def __init__(self,nombre,edad,especie,color) -> None:
        Animal.__init__(self,nombre,edad,especie,color)
    
    def __str__(self) -> str:
        return f"Serpiente: {Animal.__str__()}"
    
    def emitir_sonido(self) -> None:
         print("!!!Siseo!!")

class Condor(Animal):
    def __init__(self,nombre,edad,especie,color) -> None:
        Animal.__init__(self,nombre,edad,especie,color)
    
    def __str__(self) -> str:
        return f"Condor: {Animal.__str__()}"
    
    def emitir_sonido(self) -> None:
         print("!!!Ruido chillon!!")
    
class Rana(Animal):
    def __init__(self,nombre,edad,especie,color) -> None:
        Animal.__init__(self,nombre,edad,especie,color)
    
    def __str__(self) -> str:
        return f"Rana: {Animal.__str__()}"   
    
    def emitir_sonido(self) -> None:
         print("!!!Pitido!!")
    
class Gato(Animal):
    def __init__(self,nombre,edad,especie,color) -> None:
        Animal.__init__(self,nombre,edad,especie,color)
    
    def __str__(self) -> str:
        return f"Rana: {Animal.__str__()}"  
    
    def emitir_sonido(self) -> None:
         print("!!!Maulla!!")
    
class Perro(Animal):
    def __init__(self,nombre,edad,especie,color) -> None:
        Animal.__init__(self,nombre,edad,especie,color)
    
    def __str__(self) -> str:
        return f"Rana: {Animal.__str__()}"   
    
    def emitir_sonido(self) -> None:
         print("!!!ladra!!") 
    
# Invocaciones a los objetos

zona_anfibios = Zona_Zoologico("Zona de Anfibios","Darwin Calle")
zona_reptiles = Zona_Zoologico("Zona de Reptiles","Jose Muñoz")
zona_aves = Zona_Zoologico("Zona de Aves","Maria Emilia Sanchez")

leon_1 = Animal("Leon1",15,"Mamifero","Cafe")
leon_2 = Leon("Leon2",15,"Mamifero","Cafe","M")
rana_1 = Rana("Rana1",1,"Mamifero","Verde")

zoologico_1 = Zoologico("Zoologico1","Guallabamba","08:00 - 17:00",
                        [zona_anfibios,zona_aves,zona_reptiles],
                        [leon_1,leon_2,rana_1])

print(type(zoologico_1))
print(zoologico_1)
zoologico_1.mostrar_zonas()
zoologico_1.agregar_zona([Zona_Zoologico("Zona de Mamiferos"," Dr Suarez")])
zoologico_1.mostrar_animales()

print("*********************** Zonas *********************** ")
zoologico_1.mostrar_zonas()

print("*********************** Animales *********************** ")
zoologico_1.agregar_animal([Condor("Condor1",5,"Mamifero","Negro")])
zoologico_1.mostrar_animales()

print("*********************** Acceso a metodos protegidos *********************** ")

print (f"Facturacion : {zoologico_1.mostrar_facturacion()}")
print(f"Atributo protegido : {zoologico_1.__facturacion_valor}")