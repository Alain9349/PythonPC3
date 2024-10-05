

class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.notas = []  
        self.edad = None

    def setNota(self, nota):
        self.notas.append(nota)  

    def setAge(self, edad):
        self.edad = edad  

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        print(f"Edad: {self.edad}")
        print(f"Notas: {self.notas}")


alumno1 = Alumno("Carlos", "101487")
alumno1.setAge(25)
alumno1.setNota(16)
alumno1.setNota(18)
alumno1.setNota(15)
alumno1.display()
