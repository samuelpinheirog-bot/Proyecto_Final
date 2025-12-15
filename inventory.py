class Inventario:
    """
    Clase para manejar el inventario de productos.
    """
    def __init__(self):
        """
        Inicializa el inventario con una lista vacía de productos.
        """
        self.productos = []
        self.stock_minimo = 10  # Umbral para considerar stock bajo
    
    def agregar_producto(self, nombre, precio, cantidad):
        """
        Agrega un nuevo producto al inventario.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            cantidad (int): Cantidad en stock
        """
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(producto)
        return True
    
    def obtener_productos(self):
        """
        Obtiene la lista completa de productos.
        
        Returns:
            list: Lista de productos
        """
        return self.productos
    
    def tiene_stock_bajo(self, cantidad):
        """
        Verifica si la cantidad está por debajo del umbral mínimo.
        
        Args:
            cantidad (int): Cantidad a verificar
            
        Returns:
            bool: True si tiene stock bajo
        """
        return cantidad < self.stock_minimo
    
    def obtener_productos_stock_bajo(self):
        """
        Obtiene lista de productos con stock bajo.
        
        Returns:
            list: Lista de productos con stock bajo
        """
        return [p for p in self.productos if self.tiene_stock_bajo(p["cantidad"])]
    
    def buscar_producto(self, nombre):
        """
        Busca un producto por nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            dict or None: Producto encontrado o None
        """
        nombre_lower = nombre.lower().strip()
        for producto in self.productos:
            if nombre_lower in producto["nombre"].lower():
                return producto
        return None
    
    def actualizar_stock(self, nombre, nueva_cantidad):
        """
        Actualiza el stock de un producto.
        
        Args:
            nombre (str): Nombre del producto
            nueva_cantidad (int): Nueva cantidad en stock
            
        Returns:
            bool: True si se actualizó correctamente
        """
        producto = self.buscar_producto(nombre)
        if producto:
            producto["cantidad"] = nueva_cantidad
            return True
        return False
    
    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario.
        
        Args:
            nombre (str): Nombre del producto a eliminar
            
        Returns:
            bool: True si se eliminó correctamente
        """
        producto = self.buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False
    
    def obtener_total_productos(self):
        """
        Obtiene el número total de productos diferentes.
        
        Returns:
            int: Cantidad de productos
        """
        return len(self.productos)
    
    def obtener_valor_total(self):
        """
        Calcula el valor total del inventario.
        
        Returns:
            float: Valor total
        """
        return sum(p["precio"] * p["cantidad"] for p in self.productos)
    
    def obtener_cantidad_total(self):
        """
        Obtiene la cantidad total de unidades en inventario.
        
        Returns:
            int: Cantidad total de unidades
        """
        return sum(p["cantidad"] for p in self.productos)
