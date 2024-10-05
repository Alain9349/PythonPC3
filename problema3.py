import math  

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio 

    def calcular_area(self):
        return math.pi * (self.radio ** 2) 

#Crear 2 objetos de tipo circulo y calcular el área respectivamente

circulo1 = CIRCULO(4)  
circulo2 = CIRCULO(8)  

area_circulo1 = round(circulo1.calcular_area(),2)
area_circulo2 = round(circulo2.calcular_area(),2)

print(f"El área del círculo con radio {circulo1.radio} es: {area_circulo1}")
print(f"El área del círculo con radio {circulo2.radio} es: {area_circulo2}")