"""
- Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
constructor que recibe ambos valores.
● Definir métodos tales como:
   - eje_x
   - eje_y
   ○ impresion (método que devuelve en representación de string ambos valores)
   ○ opuesto (método que devuelve el punto opuesto -es decir con los atributos negativos-)
   ○ Cualquier otro método que considere importante
"""
# Creamos la clase punto que recibe parámetros númericos x e y
class Punto():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        
    #Definimos un metodo para recuperar el valor de x e y
    def eje_x(self):
        return self.x
    
    def eje_y(self):
        return self.y
    
    #Definimos un metodo para devolver los valores como string
    def impresion(self):
        return f"({self.x};{self.y})"
    
    #Definimos un método para devolver el punto opuesto
    def opuesto(self):
        return Punto(0 - self.x, 0 - self.y)

#Invocaciones
#Creamos los objetos
punto1 = Punto(4,2)
punto1_opuesto = punto1.opuesto()

#Mostramos en consola
print(punto1.eje_x())
print(punto1.eje_y())
print(punto1.impresion())
print(punto1_opuesto.impresion())
