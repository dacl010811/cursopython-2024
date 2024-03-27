


# Super Clase :  persona

class Persona():  # SuperClase
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self, nombre):
        print(f"Hola como estas {nombre}")
        
    def __str__(self) -> str:
        return "[{} -- {}]".format(self.nombre, self.edad)
    
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
    
    def dormir(self,):
        print("Estoy durmiendo!! - Desde la super clase!!")


# Herencia en python

class Estudiante(Persona):
    
    def __init__(self,nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso
        
    def __str__(self):
        return "Soy Estudiante : {} : [{}]".format(super().__str__(),self.curso)
        

class Empleado(Persona):
    
    def __init__(self, nombre, edad, cargo, institucion):
        super().__init__(nombre, edad)
        self.cargo = cargo 
        self.institucion = institucion       
        
    def __str__(self):
        return "Soy Empleado : {} : [{} {}]".format(super().__str__(),self.cargo,self.institucion)
    
    def registrar_biometrico(self, hora_entrada, hora_salida=17):
        
        if hora_entrada != None :
            print("Registro Satisfactorio entrada.")
        else:
            print("NO registraste el horario de entrada.")
            
        if hora_salida != None :
            print("Registro Satisfactorio Salida.")
        else:
            print("NO registraste el horario de salida.")
            
    # Definiendo  metodos de clase    
    def mostrar_cargo(cargo):
        print(f"Mi cargo es de : {cargo}")

    # Definiendo  metodos de clase
    
    @classmethod
    def mostrar_cargo(cls,cargo):
        print(f"Mi cargo es de : {cargo}")


#Instanciar las clases o Crear Objetos.

estudiante_darwin = Estudiante("Darwin",40,"Python 2024")
estudiante_darwin.envejecer(18)
print(estudiante_darwin)

estudiante_milton = Estudiante("Milton",30,"JAVA 2023")
print(estudiante_milton)

estudiante_nico = Estudiante("Nicolas Calle",4,"GO 2024")
print(estudiante_nico)

# Crear Objetos o Instacniar

empleado_1 = Empleado("Darwin Calle", 35, "Ingeniero TI","SRI")
empleado_1.dormir()
print(empleado_1) 

empleado_2 = Empleado("Martha", 55, "Ingeniero TI / Oracle", "banco Pichincha")
print(empleado_2) 

empleado_3 = Empleado("Jose", 18, "Ingeniero TI/Devops","Banco Produbanco")
print(empleado_3) 