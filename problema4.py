class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado) 
#Crear un objeto tipo rectangulo y otro tipo cuadrado
rectangulo = Rectangulo(7, 8)
print("Área del rectángulo:", rectangulo.calcular_area())  
cuadrado = Cuadrado(12)
print("Área del cuadrado:", cuadrado.calcular_area())