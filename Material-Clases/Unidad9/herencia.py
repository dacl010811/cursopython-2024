


# Super Clase :  persona

class Persona():  # SuperClase
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self, nombre):
        print(f"Hola como estas {nombre}")
    
    def envejecer(self, edad):
        if edad > 18:
            print("Eres > de edad")
        elif edad > 11 and edad < 18:
            print("Eres un adolecente")
        elif edad > 5 and edad < 10:
            print("Eres un niño")
        elif edad > 40:
            print("Eres es adulto!!")
        else:
            print("Eres un anciano")
    
    def domir(self,):
        print("Estoy durmiendo!!")


# Herencia en python

class Estudiante(Persona):
    
    def __init__(self,nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
        
    def __str__(self):
        return "Soy Estudiante : {} - {} - {}".format(self.nombre, self.edad, self.curso)
        
class Empleado(Persona):
    pass

#Instanciar las clases o Crear Objetos.

estudiante_darwin = Estudiante("Darwin",40,"Python 2024")
print(estudiante_darwin)


estudiante_milton = Estudiante("Milton",30,"Python 2023")
print(estudiante_milton)