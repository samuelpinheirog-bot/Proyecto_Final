import tkinter as tk
from tkinter import messagebox


class SistemaGestionStock:
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica del sistema de gestión de stock.
        """
        self.root = root
        self.root.title("Sistema de Gestión de Stock")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Configurar colores
        self.bg_color = "#f0f0f0"
        self.header_color = "#2c3e50"
        self.button_color = "#3498db"
        
        self.root.configure(bg=self.bg_color)
        
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """
        Crea todos los elementos de la interfaz gráfica.
        """
        # Encabezado
        header_frame = tk.Frame(self.root, bg=self.header_color, height=80)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        titulo = tk.Label(
            header_frame,
            text="SISTEMA DE GESTIÓN DE STOCK",
            font=("Arial", 18, "bold"),
            bg=self.header_color,
            fg="white",
            pady=25
        )
        titulo.pack()
        
        # Frame para los botones
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=20)
        
        # Estilo común para botones
        button_style = {
            "font": ("Arial", 12),
            "bg": self.button_color,
            "fg": "white",
            "activebackground": "#2980b9",
            "activeforeground": "white",
            "relief": tk.FLAT,
            "cursor": "hand2",
            "height": 2,
            "width": 25
        }
        
        # Botones del menú
        botones = [
            ("Agregar Producto", self.agregar_producto),
            ("Ver Inventario", self.ver_inventario),
            ("Actualizar Stock", self.actualizar_stock),
            ("Eliminar Producto", self.eliminar_producto),
            ("Buscar Producto", self.buscar_producto),
            ("Productos con Stock Bajo", self.stock_bajo),
            ("Reporte de Inventario", self.reporte_inventario),
        ]
        
        for texto, comando in botones:
            btn = tk.Button(button_frame, text=texto, command=comando, **button_style)
            btn.pack(pady=8)
        
        # Botón de salir con estilo diferente
        btn_salir = tk.Button(
            button_frame,
            text="Salir",
            command=self.salir,
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",
            height=2,
            width=25
        )
        btn_salir.pack(pady=20)
        
        # Pie de página
        footer = tk.Label(
            self.root,
            text="© 2024 Sistema de Gestión de Stock",
            font=("Arial", 9),
            bg=self.bg_color,
            fg="#7f8c8d"
        )
        footer.pack(side=tk.BOTTOM, pady=10)
    
    def agregar_producto(self):
        """
        Función para agregar un nuevo producto.
        """
        messagebox.showinfo(
            "Agregar Producto",
            "Funcionalidad 'Agregar Producto'\n(Pendiente de implementación)"
        )
    
    def ver_inventario(self):
        """
        Función para ver todos los productos del inventario.
        """
        messagebox.showinfo(
            "Ver Inventario",
            "Funcionalidad 'Ver Inventario'\n(Pendiente de implementación)"
        )
    
    def actualizar_stock(self):
        """
        Función para actualizar el stock de un producto.
        """
        messagebox.showinfo(
            "Actualizar Stock",
            "Funcionalidad 'Actualizar Stock'\n(Pendiente de implementación)"
        )
    
    def eliminar_producto(self):
        """
        Función para eliminar un producto del inventario.
        """
        messagebox.showinfo(
            "Eliminar Producto",
            "Funcionalidad 'Eliminar Producto'\n(Pendiente de implementación)"
        )
    
    def buscar_producto(self):
        """
        Función para buscar un producto específico.
        """
        messagebox.showinfo(
            "Buscar Producto",
            "Funcionalidad 'Buscar Producto'\n(Pendiente de implementación)"
        )
    
    def stock_bajo(self):
        """
        Función para mostrar productos con stock bajo.
        """
        messagebox.showinfo(
            "Stock Bajo",
            "Funcionalidad 'Productos con Stock Bajo'\n(Pendiente de implementación)"
        )
    
    def reporte_inventario(self):
        """
        Función para generar reporte de inventario.
        """
        messagebox.showinfo(
            "Reporte de Inventario",
            "Funcionalidad 'Reporte de Inventario'\n(Pendiente de implementación)"
        )
    
    def salir(self):
        """
        Función para cerrar la aplicación.
        """
        respuesta = messagebox.askyesno(
            "Salir",
            "¿Está seguro que desea salir del sistema?"
        )
        if respuesta:
            self.root.quit()


def main():
    """
    Función principal que inicia la aplicación.
    """
    root = tk.Tk()
    app = SistemaGestionStock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
