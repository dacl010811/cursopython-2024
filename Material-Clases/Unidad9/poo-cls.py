



class Circulo():
    
    # Atributo de clase
    pi = 3.14159
       
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area_circulo(self):
        return self.pi * (self.radio**2)

    # Metodo de clase
    @classmethod
    def obtener_valor_pi(cls):
        return cls.pi

# Con esto invocabamos a los atributos y metodos de instancias
circulo = Circulo(5.879)
print(circulo.radio)
print(f"El area del circulo es = {circulo.calcular_area_circulo()}")

# Atributos y Metodos de Clase
print(Circulo.pi)
print(Circulo.obtener_valor_pi())




