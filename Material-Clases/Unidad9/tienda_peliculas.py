


class Pelicula():
    
    def __init__(self, titulo, duracion, lanzamiento,tipo,autor,annio) -> None:
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.tipo = tipo
        self.autor = autor
        self.annio = annio
    
    def __str__(self) -> str:
        return f"Pelicula: [{self.titulo},{self.autor}]"
        

class Catalogo():
    
    peliculas = [("Super Man",120,2020,"Accion","DC","2021")]
    
    def __init__(self,nombre, peliculas=None):
        if peliculas:
            self.peliculas = peliculas
    
    def agregar_pelicula(self,nueva_pelicula):
        self.peliculas.append(nueva_pelicula)
        
    def mostrar_catalogo(self):
        for p in self.peliculas:
            print(f"Pelicula: {p.titulo}, {p.autor}, {p.annio}")
        

#Invocacion

lista_peliculas = []

pelicula_1 = Pelicula("Avengers 1",120,2020,"Accion","Disney","2021")
pelicula_2 = Pelicula("Hombre Araña 1",180,2020,"Accion","Disney","2021")
pelicula_3 = Pelicula("ANT ",360,2020,"Accion","Disney","2021")

lista_peliculas.append(pelicula_1)
lista_peliculas.append(pelicula_2)
lista_peliculas.append(pelicula_3)


catalogo_1 = Catalogo("Catalogo 2024",lista_peliculas)
catalogo_1.mostrar_catalogo()


pelicula_4 = Pelicula("ANT 2",360,2020,"Accion","Disney","2021")
catalogo_1.agregar_pelicula(pelicula_4)
print("*********************")
catalogo_1.mostrar_catalogo()

print(Catalogo.peliculas)



