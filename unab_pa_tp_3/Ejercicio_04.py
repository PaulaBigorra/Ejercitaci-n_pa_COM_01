"""
Desarrolla una clase Cancion con los siguientes atributos:
  - titulo: una variable String que guarda el título de la canción.
  - autor: una variable String que guarda el autor de la canción.
Con los siguientes métodos:
  - Cancion(String, String): constructor que recibe como parámetros el título y el autor de la canción (por este orden). 
  - get_titulo(): devuelve el título de la canción.
  - get_autor(): devuelve el autor de la canción.
  - set_titulo(String): establece el título de la canción.
  - set_autor(String): establece el autor de la canción.
"""

#Creamos la clase Cancion.
class Cancion():
    def __init__(self, titulo, autor):
        self.__titulo = titulo;
        self.__autor = autor;
    
    #Definimos un método para recuperar el titulo.
    def get_titulo(self):
        return self.__titulo
    
    #Definimos un método para recuperar el autor.
    def get_autor(self):
        return self.__autor
    
    #Definimos un método para redefinir el titulo.
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    #Definimos un método para redefinir el autor.
    def set_autor(self, autor):
        self.__autor = autor

#Creamos una canción.
song1 = Cancion("Desde el mañana", "augusto ramiro")

#Mostramos en consola los atributos de la canción utilizando los métodos correspondientes.
print(song1.get_titulo())
print(song1.get_autor())

#Redefinimos los atributos titulo y autor con los métodos correspondientes.
song1.set_titulo("Desde el ayer")
song1.set_autor("fabricio equiparte")
