
import json


class  Persona():
    
    __estado_tributario = "Deudas Firmes" # Encapsulamiento
    
    def __init__(self, nombre, ruc) -> None:
        self.nombre = nombre
        self.ruc = ruc
        
    def mostrar_estado_tributario(self):
        print("Usted presenta deudas firmes con el estado")
        
    def __monto_deuda(self):             # Encapsulamiento
        return "Usted adeuda $1000000"
    
    def mostrar_monto_deuda(self):
        return self.__monto_deuda()
    
    
    def estado_tributario(self):
        return self.__estado_tributario
    
    def guardar(self): 
        print("Guardando")       
        if isinstance(super().__init__(),Persona):
            diccionario = self.__dict__
            if diccionario:
                print("Hay datos")
                with open("persona.json","w") as fjson:
                    json.dump([diccionario],fjson)
            else:
                print("No hay datos para guardar")
            

#Invocacion

persona_1 = Persona("Darwin Calle","1104258877")
persona_1.guardar()

#print(Persona.__estado_tributario)
#print(Persona.__monto_deuda())

#print(persona_1.__estado_tributario)
#print(persona_1.__monto_deuda())

#print(persona_1.estado_tributario())
#print(persona_1.mostrar_monto_deuda())


        
    