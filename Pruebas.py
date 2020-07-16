import math
class Figura:
    Tipo_figura = "Plana "
    def __init__(self,Lados ,  Longuitud):
        self.Lados = Lados
        self.Longuitud = Longuitud
        self.Nombre = []
    def Perimetro(self):
        print (f"el Perimetro es {self.Lados *  self.Longuitud}")
    def Area (self):
        angulo= math.pi/self.Lados
        area= (self.Lados* (self.Longuitud**2))/(4*math.tan(angulo))
        print(f"esta es su area {angulo}")


Cuadrado=Figura(4,8)
Cuadrado.Perimetro()
Cuadrado.Area()
