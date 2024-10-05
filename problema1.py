def fraccion():
    while True:
        try:
            solicitar_fraccion = input("Introduce una fraccion en formato X/Y: ")
            x, y = map(int, solicitar_fraccion .split('/'))  
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser cero.Intentalo de nuevo.")
                
            if x > y:
                print("X debe ser menor o igual a Y. Intentalo de nuevo.")
                continue
            porcentaje = (x / y) * 100

            if porcentaje > 99:
                return "F"
            elif porcentaje < 1:
                return "E"
            else:
                return f"{round(porcentaje)}%"
        
        except ValueError:
            print("Error dado que solo se permiten números enteros.")
        except ZeroDivisionError as error:
            print(error)

resultado =fraccion()
print("Resultado:", resultado)