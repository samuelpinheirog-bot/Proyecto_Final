import tkinter as tk
from tkinter import messagebox
from utils import validar_nombre, validar_precio, validar_cantidad


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
        Abre una ventana secundaria con formulario de entrada.
        """
        # Crear ventana secundaria
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")
        ventana.geometry("400x300")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        # Centrar la ventana
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Título
        titulo = tk.Label(
            ventana,
            text="Agregar Nuevo Producto",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        )
        titulo.pack(pady=20)
        
        # Frame para el formulario
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=30, pady=10)
        
        # Campo Nombre
        tk.Label(form_frame, text="Nombre:", font=("Arial", 10), bg=self.bg_color).grid(
            row=0, column=0, sticky="w", pady=10
        )
        entry_nombre = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry_nombre.grid(row=0, column=1, pady=10, padx=10)
        entry_nombre.focus()
        
        # Campo Precio
        tk.Label(form_frame, text="Precio:", font=("Arial", 10), bg=self.bg_color).grid(
            row=1, column=0, sticky="w", pady=10
        )
        entry_precio = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry_precio.grid(row=1, column=1, pady=10, padx=10)
        
        # Campo Cantidad
        tk.Label(form_frame, text="Cantidad:", font=("Arial", 10), bg=self.bg_color).grid(
            row=2, column=0, sticky="w", pady=10
        )
        entry_cantidad = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry_cantidad.grid(row=2, column=1, pady=10, padx=10)
        
        # Frame para botones
        button_frame = tk.Frame(ventana, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        def guardar_producto():
            """Valida y guarda el producto."""
            nombre = entry_nombre.get()
            precio_str = entry_precio.get()
            cantidad_str = entry_cantidad.get()
            
            # Validar nombre
            valido, mensaje = validar_nombre(nombre)
            if not valido:
                messagebox.showerror("Error de Validación", mensaje, parent=ventana)
                entry_nombre.focus()
                return
            
            # Validar precio
            valido, resultado = validar_precio(precio_str)
            if not valido:
                messagebox.showerror("Error de Validación", resultado, parent=ventana)
                entry_precio.focus()
                return
            precio = resultado
            
            # Validar cantidad
            valido, resultado = validar_cantidad(cantidad_str)
            if not valido:
                messagebox.showerror("Error de Validación", resultado, parent=ventana)
                entry_cantidad.focus()
                return
            cantidad = resultado
            
            # Si todas las validaciones pasaron
            messagebox.showinfo(
                "Éxito",
                f"Producto agregado correctamente:\n\n"
                f"Nombre: {nombre.strip()}\n"
                f"Precio: ${precio:.2f}\n"
                f"Cantidad: {cantidad}",
                parent=ventana
            )
            ventana.destroy()
        
        # Botón Guardar
        btn_guardar = tk.Button(
            button_frame,
            text="Guardar",
            command=guardar_producto,
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            width=12,
            cursor="hand2"
        )
        btn_guardar.pack(side=tk.LEFT, padx=5)
        
        # Botón Cancelar
        btn_cancelar = tk.Button(
            button_frame,
            text="Cancelar",
            command=ventana.destroy,
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            width=12,
            cursor="hand2"
        )
        btn_cancelar.pack(side=tk.LEFT, padx=5)
    
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
        Abre una ventana secundaria con formulario de entrada.
        """
        # Crear ventana secundaria
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Stock")
        ventana.geometry("400x250")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        # Centrar la ventana
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Título
        titulo = tk.Label(
            ventana,
            text="Actualizar Stock de Producto",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        )
        titulo.pack(pady=20)
        
        # Frame para el formulario
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=30, pady=10)
        
        # Campo Nombre del producto
        tk.Label(form_frame, text="Nombre del Producto:", font=("Arial", 10), bg=self.bg_color).grid(
            row=0, column=0, sticky="w", pady=10
        )
        entry_nombre = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry_nombre.grid(row=0, column=1, pady=10, padx=10)
        entry_nombre.focus()
        
        # Campo Nueva Cantidad
        tk.Label(form_frame, text="Nueva Cantidad:", font=("Arial", 10), bg=self.bg_color).grid(
            row=1, column=0, sticky="w", pady=10
        )
        entry_cantidad = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry_cantidad.grid(row=1, column=1, pady=10, padx=10)
        
        # Frame para botones
        button_frame = tk.Frame(ventana, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        def actualizar():
            """Valida y actualiza el stock."""
            nombre = entry_nombre.get()
            cantidad_str = entry_cantidad.get()
            
            # Validar nombre
            valido, mensaje = validar_nombre(nombre)
            if not valido:
                messagebox.showerror("Error de Validación", mensaje, parent=ventana)
                entry_nombre.focus()
                return
            
            # Validar cantidad
            valido, resultado = validar_cantidad(cantidad_str)
            if not valido:
                messagebox.showerror("Error de Validación", resultado, parent=ventana)
                entry_cantidad.focus()
                return
            cantidad = resultado
            
            # Si todas las validaciones pasaron
            messagebox.showinfo(
                "Éxito",
                f"Stock actualizado correctamente:\n\n"
                f"Producto: {nombre.strip()}\n"
                f"Nueva Cantidad: {cantidad}",
                parent=ventana
            )
            ventana.destroy()
        
        # Botón Actualizar
        btn_actualizar = tk.Button(
            button_frame,
            text="Actualizar",
            command=actualizar,
            font=("Arial", 10, "bold"),
            bg="#27ae60",
            fg="white",
            width=12,
            cursor="hand2"
        )
        btn_actualizar.pack(side=tk.LEFT, padx=5)
        
        # Botón Cancelar
        btn_cancelar = tk.Button(
            button_frame,
            text="Cancelar",
            command=ventana.destroy,
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            width=12,
            cursor="hand2"
        )
        btn_cancelar.pack(side=tk.LEFT, padx=5)
    
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
        Abre una ventana secundaria con formulario de búsqueda.
        """
        # Crear ventana secundaria
        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar Producto")
        ventana.geometry("400x200")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        # Centrar la ventana
        ventana.transient(self.root)
        ventana.grab_set()
        
        # Título
        titulo = tk.Label(
            ventana,
            text="Buscar Producto",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        )
        titulo.pack(pady=20)
        
        # Frame para el formulario
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=30, pady=10)
        
        # Campo Nombre
        tk.Label(form_frame, text="Nombre del Producto:", font=("Arial", 10), bg=self.bg_color).grid(
            row=0, column=0, sticky="w", pady=10
        )
        entry_nombre = tk.Entry(form_frame, font=("Arial", 10), width=25)
        entry_nombre.grid(row=0, column=1, pady=10, padx=10)
        entry_nombre.focus()
        
        # Frame para botones
        button_frame = tk.Frame(ventana, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        def buscar():
            """Valida y busca el producto."""
            nombre = entry_nombre.get()
            
            # Validar nombre
            valido, mensaje = validar_nombre(nombre)
            if not valido:
                messagebox.showerror("Error de Validación", mensaje, parent=ventana)
                entry_nombre.focus()
                return
            
            # Si la validación pasó
            messagebox.showinfo(
                "Búsqueda",
                f"Buscando producto: {nombre.strip()}\n\n"
                f"(Funcionalidad de búsqueda pendiente de implementación)",
                parent=ventana
            )
            ventana.destroy()
        
        # Botón Buscar
        btn_buscar = tk.Button(
            button_frame,
            text="Buscar",
            command=buscar,
            font=("Arial", 10, "bold"),
            bg=self.button_color,
            fg="white",
            width=12,
            cursor="hand2"
        )
        btn_buscar.pack(side=tk.LEFT, padx=5)
        
        # Botón Cancelar
        btn_cancelar = tk.Button(
            button_frame,
            text="Cancelar",
            command=ventana.destroy,
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            width=12,
            cursor="hand2"
        )
        btn_cancelar.pack(side=tk.LEFT, padx=5)
    
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
