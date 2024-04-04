class Persona:
    """ Representa la clase Persona """

    def __init__(self, nombre, apellido, cedula, email, telefono):
        """Constructor de la clase Persona"""
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return "Persona: [{} {} {} {} {}]".format(self.nombre, self.apellido, self.cedula, self.email, self.telefono)

class Cliente(Persona):
    """Cliente

    Args:
        Persona (Persona): Hereda de la clase persona
    """       
    def __init__(self, nombre, apellido, cedula, email, telefono,dirección, sector,celular):
        """Constructor
        Args:
            nombre (str): Representa el nombre
            apellido (str): Representa el apellido
            cedula (str): Representa  la cedula
            email (str): Representa el correo
            telefono (str): Representa  un telefono
            direccion (str): Representa el direccion
            sector (str): Representa el sector
            celular (str): Representa el celular
        """               
        Persona.__init__(self, nombre, apellido, cedula, email, telefono)        
        self.dirección = dirección
        self.sector = sector
        self.celular = celular

    def __str__(self):
        return "Cliente: [{} {} {} {}]".format(super().__str__(),self.dirección, self.sector,self.celular)
    