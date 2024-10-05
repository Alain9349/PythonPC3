calificaciones_separadas = input("Introduce las calificaciones separadas por comas: ")
lista_de_clasificaciones = calificaciones_separadas.split(",")
calificaciones_enteras = []

for calificacion in lista_de_clasificaciones :
    try:
        calificacion_entera = int(calificacion)
        calificaciones_enteras.append(calificacion_entera)
    except ValueError:
        print(f"Error: '{calificacion}' los valores introducidos no puedan ser convertidos debido a un error de tipeo o formato.")

print("Calificaciones válidas:", calificaciones_enteras)