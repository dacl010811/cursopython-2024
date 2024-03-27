

class Persona():
    
    """ Esta clase representa un plantilla para generar objetos de tipo <Persona>
    """    
    
    def __init__(self,nombre, numero_telefono, email):
        """Constructor para crear objetos de tipo <Persona>
        Args:
            nombre (str): Representa el nombre
            numero_telefono (str): Representa el numero de telefono
            email (str): Representa el email
        """        
        self.nombre = nombre
        self.numero_telefono = numero_telefono
        self.email = email

    def saludar(self, mensaje):
        """Metodo para saludar

        Args:
            mensaje (str): Saludo a enviar
        """        
        print (f"{mensaje} : {self.nombre}")
    
    def dormir(self):
        """Metodo dormir
        """        
        print(f"Buenas noches - {self.nombre}")
    
    def correr(self):
        print(f"Inicia la carrera - {self.nombre}")
    
    def comer(self):
        print(f"Estas cenando - {self.nombre}")
        
    def __str__(self):
        return "str: Persona: [{} {} {}]".format(self.nombre, self.numero_telefono, self.email)
    

class Direccion():
    
    #Atributo de clase
    gps = '0º 120 12º 12º'
        
    def __init__(self,calle,ciudad,provincia, codigo_postal,pais):
        """_summary_

        Args:
            calle (_type_): _description_
            ciudad (_type_): _description_
            provincia (_type_): _description_
            codigo_postal (_type_): _description_
            pais (_type_): _description_
        """                             
        self.calle = calle
        self.ciudad = ciudad
        self.provincia = provincia
        self.codigo_postal = codigo_postal
        self.pais = pais
    
    def obtener_postal(self):
        return self.codigo_postal
    
    def obtener_provincia(self):
        return self.provincia   
        
    def obtener_pais(self):
        return self.pais
    
    #Metodo de clase
    @classmethod
    def obtener_gps(cls):
        return cls.gps
    
    

class Estudiante():
    pass

class Profesor(Persona):
    def __init__(self):
        super().__init__()
        
    
#Instanciar las clases o crear objetos
persona_1 = Persona("Darwin Calle1","09988775521","dacl010811@gmail.com")
print(persona_1)
persona_2 = Persona("Darwin Calle2","09988775521","dacl010812@gmail.com")
print(persona_2)
persona_3 = Persona("Darwin Calle3","09988775521","dacl010813@gmail.com")
print(persona_3)