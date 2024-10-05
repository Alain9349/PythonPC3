#Crea una clase llamada punto con sus dos coordenadas X e Y
class Punto:

#Metodo constructor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

#Sobreescribe el metodo string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
#Metodo cuandrante

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Está en el origen"
        elif self.x == 0:
            return "Está sobre el eje Y"
        elif self.y == 0:
            return "Está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Cuadrante I"
        elif self.x < 0 < self.y:
            return "Cuadrante II"
        elif self.x < 0 and self.y < 0:
            return "Cuadrante III"
        else:
            return "Cuadrante IV"
        
#Metodo vector
#Ejemplo: •	AB = (x2 - x1, y2 - y1) => (5-2, 5-3) => (3,2)

    def vector(self, otro_punto):
        return (otro_punto.x - self.x, otro_punto.y - self.y)
    
#Metodo distancia
    def distancia(self, otro_punto):
        return ((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2) ** 0.5

#Clase Rectangulo con dos puntos (inicial y final)
class Rectangulo:
    def __init__(self, punto_inicial=Punto(0, 0), punto_final=Punto(0, 0)):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
#Metodo base:
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
#Metodo altura:
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
#AMetodo area:
    def area(self):
        return self.base() * self.altura()
    
###Experimentacion
#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

print(A)  
print(B)  
print(C)  
print(D)  

#Consulta a que cuadrante pertenecen el punto A, C y D.
print(A.cuadrante())  
print(C.cuadrante())  
print(D.cuadrante())  

#Calcular la distancia entre los puntos A y B, y B y A

distancia_A_B = A.distancia(B)
distancia_B_A = B.distancia(A)

print(f"Distancia entre A y B: {distancia_A_B}")
print(f"Distancia entre B y A: {distancia_B_A}")

#Determinar cual de los puntos A, B, C está más lejos del origen

distancia_A = A.distancia(D)
distancia_B = B.distancia(D)
distancia_C = C.distancia(D)

max_distancia = max(distancia_A, distancia_B, distancia_C)

if max_distancia == distancia_A:
    print("El punto A está más lejos del origen.")
elif max_distancia == distancia_B:
    print("El punto B está más lejos del origen.")
else:
    print("El punto C está más lejos del origen.")

#Crear el rectangulo utilizando los puntos A y B

rectangulo = Rectangulo(A, B)

print(f"Base del rectángulo: {rectangulo.base()}")
print(f"Altura del rectángulo: {rectangulo.altura()}")
print(f"Área del rectángulo: {rectangulo.area()}")

