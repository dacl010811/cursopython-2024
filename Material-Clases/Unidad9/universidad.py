
import json


class Persona():

    """ Esta clase representa un plantilla para generar objetos de tipo <Persona>
    """

    def __init__(self, nombre, numero_telefono, email):
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
        print(f"{mensaje} : {self.nombre}")

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

    def guardar(self, datos):
        print(type(datos))
        with open("bdd.json", "w") as fjson:
            json.dump(datos, fjson)


class Direccion():

    # Atributo de clase
    gps = '0º 120 12º 12º'

    def __init__(self, calle, ciudad, provincia, codigo_postal, pais):
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

    # Metodo de clase
    @classmethod
    def obtener_gps(cls):
        return cls.gps


class Estudiante(Persona):
    def __init__(self, nombre, numero_telefono, email, universidad, modulo, pension):
        super().__init__(nombre, numero_telefono, email)

        self.universidad = universidad
        self.modulo = modulo
        self.pension = pension

    def __str__(self):
        return f"Estudiante : {super().__str__()} {self.universidad},{self.modulo},{self.pension}"


class Profesor(Persona):
    def __init__(self, nombre, numero_telefono, email, institucion, salario, tiempo):
        super().__init__(nombre, numero_telefono, email)

        self.institucion = institucion
        self.salario = salario
        self.tiempo = tiempo

    def __str__(self):
        return f"Profesor : {super().__str__()} {self.institucion} {self.salario} {self.tiempo}"


class FuncionarioPublico(Persona, Direccion):

    def __init__(self, nombre, numero_telefono, email, calle, ciudad, provincia, codigo_postal, pais, institucion_publica, tiempo_servicio, departamento, coordinacion, atributoDefecto=None):

        # super().__init__(nombre, numero_telefono, email)

        Persona.__init__(self, nombre, numero_telefono, email)
        Direccion.__init__(self, calle, ciudad, provincia, codigo_postal, pais)

        self.institucion_publica = institucion_publica
        self.tiempo_servicio = tiempo_servicio
        self.departamento = departamento
        self.coordinacion = coordinacion
        self.atributoDefecto = atributoDefecto

    def __str__(self):        
        return f" : {Persona.__str__(self)} {Direccion.__str__(self)} Funcionario: [{self.institucion_publica},{self.tiempo_servicio},{self.departamento},{self.coordinacion}]"


# Instanciar las clases o crear objetos
datos = []

estudiante_1 = Estudiante("Darwin Calle", "09955877544",
                          "dacl010812@gmail.com", "UNL", "Sexto Modulo", 200)
estudiante_2 = Estudiante("NIco Calle", "09955877544",
                          "dacl010813@gmail.com", "UNL", "Quinto Modulo", 200)
estudiante_3 = Estudiante("Martha Calle", "09955877544",
                          "dacl010816@gmail.com", "UNL", "NOveno Modulo", 200)

"""print(estudiante_1.__dict__)
print(vars(estudiante_2))
print(estudiante_3.__dict__)"""

funcionario_1 = FuncionarioPublico("David", "0998522244", "dacl@gmail.com", "Av Maestro",
                                   "Loja", "Loja", "00245", "Ecuador", "SRI", "10", "Seguridad", "Seguridad INFO")
#print(funcionario_1.__dict__)

funcionario_2 = FuncionarioPublico("NIcolas", "0998522244", "dacl@gmail.com", "Av Maestro",
                                   "Quito", "Quito", "00245", "Ecuador", "SRI", "10", "Seguridad", "Seguridad INFO")

#print(vars(funcionario_2))

print(estudiante_1)

datos.append(estudiante_1.__dict__)
datos.append(vars(estudiante_2))
datos.append(estudiante_3.__dict__)

with open("estudiantes.json","w") as fileJSON:
    json.dump(datos, fileJSON)
    


