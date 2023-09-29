class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def eliminarProducto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                print(f"Producto eliminado del inventario.")
                return
        print(f"No se encontro el producto en el inventario.")

    def mostrarInventario(self):
        if not self.productos:
            print("El inventario está vacio.")
        else:
            print("Inventario:")
            for producto in self.productos:
                print(producto)


producto1 = Producto(1, "Notebook", 1000)
producto2 = Producto(2, "Celular", 300)
producto3 = Producto(3, "Monitor", 200)

inventario = Inventario()

inventario.agregarProducto(producto1)
inventario.agregarProducto(producto2)
inventario.agregarProducto(producto3)

inventario.mostrarInventario()

inventario.eliminarProducto(1)

inventario.mostrarInventario()
