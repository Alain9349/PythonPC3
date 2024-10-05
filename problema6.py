
class Catalogo_y_Producto:
    def __init__(self, nombre, año, modelo, precio):
        self.nombre = nombre
        self.año= año
        self.modelo = modelo
        self.precio = precio
    
    def __str__(self):
        return f"{self.nombre} ({self.año}) - {self.modelo}: S/.{self.precio}"

class Catalogo:
    def __init__(self):
        self.productos = [] 

    def agregar_producto(self, producto):
        self.productos.append(producto)  

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
        else:
            for producto in self.productos:
                print(producto)  


catalogo_autopartes = Catalogo()

producto1 = Catalogo_y_Producto("Filtro de aceite", 2021, "Creta", 53.26)
producto2 = Catalogo_y_Producto("Bujías", 2022, "Accent", 68.55)
producto3 = Catalogo_y_Producto("Kit de Embrague", 2019, "Hyundai", 270.55)

catalogo_autopartes.agregar_producto(producto1)
catalogo_autopartes.agregar_producto(producto2)
catalogo_autopartes.agregar_producto(producto3)

catalogo_autopartes.mostrar_productos()