from gestion import GestionBiblioteca
from libro import Libro

def main():
    gestion = GestionBiblioteca()
    
    while True:
        print("\nMenu:")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Buscar libro por titulo")
        print("4. Buscar libro por autor")
        print("5. Salir")
        
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor,isbn)
            gestion.agregar_libro(libro)
            print("Libro agregado.")
        
        elif opcion == "2":
            print("Lista de libros:")
            gestion.listar_libros()
        
        elif opcion == "3":
            titulo = input("Ingrese el titulo a buscar: ")
            gestion.buscar_por_titulo(titulo)
        
        elif opcion == "4":
            autor = input("Ingrese el autor a buscar: ")
            gestion.buscar_por_autor(autor)
        
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opcion no valida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
