"""
Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que pasa la línea en un espacio de dos dimensiones. 
La clase dispondrá de los siguientes métodos:
  - Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase.
Punto, que son utilizados para inicializar los atributos.
  - mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
  - mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
  - mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
  - mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.
"""

#Importamos la clase Punto() del módulo "Ejercicio_2".
from Ejercicio_2 import Punto

#Creamos la clase Linuea() que recibe como parámetros los objetos Punto creados con la clase Punto().
class Linea():
    def __init__(self,_punto_a,_punto_b):
        self._punto_a = _punto_a;
        self._punto_b = _punto_b;
    
    #Definimos metodos para mover hacia la derecha o izquierda la linea modificando el atributo x de los puntos.
    def mueve_derecha(self, num):
        self._punto_a.x += num
        self._punto_b.x += num
    
    def mueve_izquierda(self, num):
        self._punto_a.x -= num
        self._punto_b.x -= num
    
    #Definimos metodos para mover hacia la arriba o abajo la linea modificando el atributo y de los puntos.
    def mueve_arriba(self, num):
        self._punto_a.y += num
        self._punto_b.y += num
        
    def mueve_abajo(self, num):
        self._punto_a.y -= num
        self._punto_b.y -= num

#Creamos puntos con la clase Punto()
punto1 = Punto(4, 2)
punto2 = Punto(8,4)

#Creamos la linea utilizando como parámetros los puntos definidos
linea1 = Linea(punto1, punto2)

#Utilizamos los métodos para desplazar la linea
linea1.mueve_derecha(2)
linea1.mueve_izquierda(6)
linea1.mueve_arriba(8)
linea1.mueve_abajo(1)

#print(linea1._punto_a.y, linea1._punto_b.y)
