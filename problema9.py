
import math

def validar_numero(numero):
    try:
        valor = float(numero)
        if valor > 0:
            return valor
        else:
            print("Por favor, ingrese un número positivo.")
            return None
    except ValueError:
        print("Entrada no válida. Debe ser un número.")
        return None

def area_circulo():
    radio = input("Ingrese el radio del círculo: ")
    radio = validar_numero(radio)
    if radio is not None:
        area = math.pi * (radio ** 2)
        print(f"El área del círculo con radio {radio} es: {area}")

def area_rectangulo():
    largo = input("Ingrese el largo del rectángulo: ")
    ancho = input("Ingrese el ancho del rectángulo: ")
    largo = validar_numero(largo)
    ancho = validar_numero(ancho)
    if largo is not None and ancho is not None:
        area = largo * ancho
        print(f"El área del rectángulo de largo {largo} y ancho {ancho} es: {area}")

def area_cuadrado():
    lado = input("Ingrese el lado del cuadrado: ")
    lado = validar_numero(lado)
    if lado is not None:
        area = lado ** 2
        print(f"El área del cuadrado con lado {lado} es: {area}")

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            area_circulo()
        elif opcion == '2':
            area_rectangulo()
        elif opcion == '3':
            area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()