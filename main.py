import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from inventory import Inventario


class SistemaGestionStock:
    def __init__(self, root):
        """
        Inicializa la interfaz gráfica del sistema de gestión de stock.
        """
        self.root = root
        self.root.title("Sistema de Gestión de Stock")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Inicializar inventario
        self.inventario = Inventario()
        
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
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Producto")
        ventana.geometry("400x300")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        # Título
        tk.Label(
            ventana,
            text="Nuevo Producto",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=20)
        
        # Frame para el formulario
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=40, pady=10)
        
        # Campo nombre
        tk.Label(form_frame, text="Nombre:", font=("Arial", 10), bg=self.bg_color).grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = tk.Entry(form_frame, font=("Arial", 10), width=30)
        entry_nombre.grid(row=0, column=1, pady=5)
        
        # Campo precio
        tk.Label(form_frame, text="Precio:", font=("Arial", 10), bg=self.bg_color).grid(row=1, column=0, sticky="w", pady=5)
        entry_precio = tk.Entry(form_frame, font=("Arial", 10), width=30)
        entry_precio.grid(row=1, column=1, pady=5)
        
        # Campo cantidad
        tk.Label(form_frame, text="Cantidad:", font=("Arial", 10), bg=self.bg_color).grid(row=2, column=0, sticky="w", pady=5)
        entry_cantidad = tk.Entry(form_frame, font=("Arial", 10), width=30)
        entry_cantidad.grid(row=2, column=1, pady=5)
        
        def guardar():
            nombre = entry_nombre.get().strip()
            precio_str = entry_precio.get().strip()
            cantidad_str = entry_cantidad.get().strip()
            
            if not nombre or not precio_str or not cantidad_str:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            try:
                precio = float(precio_str)
                cantidad = int(cantidad_str)
                
                if precio <= 0 or cantidad < 0:
                    messagebox.showerror("Error", "El precio debe ser mayor a 0 y la cantidad no puede ser negativa")
                    return
                
                self.inventario.agregar_producto(nombre, precio, cantidad)
                messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente")
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Precio y cantidad deben ser números válidos")
        
        # Botones
        btn_frame = tk.Frame(ventana, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Guardar",
            command=guardar,
            bg=self.button_color,
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Cancelar",
            command=ventana.destroy,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
    
    def ver_inventario(self):
        """
        Función para ver todos los productos del inventario.
        """
        productos = self.inventario.obtener_productos()
        
        if not productos:
            messagebox.showinfo("Inventario Vacío", "No hay productos en el inventario")
            return
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Ver Inventario")
        ventana.geometry("700x500")
        ventana.configure(bg=self.bg_color)
        
        # Título
        tk.Label(
            ventana,
            text="Inventario de Productos",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=15)
        
        # Frame para la tabla
        frame = tk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        tree = ttk.Treeview(
            frame,
            columns=("Nombre", "Precio", "Cantidad", "Total"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=tree.yview)
        
        # Configurar columnas
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio ($)")
        tree.heading("Cantidad", text="Cantidad")
        tree.heading("Total", text="Valor Total ($)")
        
        tree.column("Nombre", width=250)
        tree.column("Precio", width=100, anchor="center")
        tree.column("Cantidad", width=100, anchor="center")
        tree.column("Total", width=120, anchor="center")
        
        # Agregar productos
        for producto in productos:
            total = producto["precio"] * producto["cantidad"]
            tree.insert("", tk.END, values=(
                producto["nombre"],
                f"{producto['precio']:.2f}",
                producto["cantidad"],
                f"{total:.2f}"
            ))
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Resumen
        total_productos = self.inventario.obtener_total_productos()
        total_unidades = self.inventario.obtener_cantidad_total()
        valor_total = self.inventario.obtener_valor_total()
        
        resumen_frame = tk.Frame(ventana, bg=self.bg_color)
        resumen_frame.pack(pady=10)
        
        tk.Label(
            resumen_frame,
            text=f"Total productos: {total_productos} | Total unidades: {total_unidades} | Valor total: ${valor_total:.2f}",
            font=("Arial", 10, "bold"),
            bg=self.bg_color
        ).pack()
    
    def actualizar_stock(self):
        """
        Función para actualizar el stock de un producto.
        """
        productos = self.inventario.obtener_productos()
        
        if not productos:
            messagebox.showinfo("Inventario Vacío", "No hay productos en el inventario")
            return
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Stock")
        ventana.geometry("400x250")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        tk.Label(
            ventana,
            text="Actualizar Stock",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=20)
        
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=40, pady=10)
        
        tk.Label(form_frame, text="Producto:", font=("Arial", 10), bg=self.bg_color).grid(row=0, column=0, sticky="w", pady=5)
        
        combo_productos = ttk.Combobox(
            form_frame,
            values=[p["nombre"] for p in productos],
            font=("Arial", 10),
            width=28,
            state="readonly"
        )
        combo_productos.grid(row=0, column=1, pady=5)
        
        tk.Label(form_frame, text="Nueva Cantidad:", font=("Arial", 10), bg=self.bg_color).grid(row=1, column=0, sticky="w", pady=5)
        entry_cantidad = tk.Entry(form_frame, font=("Arial", 10), width=30)
        entry_cantidad.grid(row=1, column=1, pady=5)
        
        def actualizar():
            nombre = combo_productos.get()
            cantidad_str = entry_cantidad.get().strip()
            
            if not nombre or not cantidad_str:
                messagebox.showerror("Error", "Debe seleccionar un producto e ingresar una cantidad")
                return
            
            try:
                cantidad = int(cantidad_str)
                
                if cantidad < 0:
                    messagebox.showerror("Error", "La cantidad no puede ser negativa")
                    return
                
                if self.inventario.actualizar_stock(nombre, cantidad):
                    messagebox.showinfo("Éxito", f"Stock de '{nombre}' actualizado a {cantidad} unidades")
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el stock")
                    
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número válido")
        
        btn_frame = tk.Frame(ventana, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Actualizar",
            command=actualizar,
            bg=self.button_color,
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Cancelar",
            command=ventana.destroy,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
    
    def eliminar_producto(self):
        """
        Función para eliminar un producto del inventario.
        """
        productos = self.inventario.obtener_productos()
        
        if not productos:
            messagebox.showinfo("Inventario Vacío", "No hay productos en el inventario")
            return
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Producto")
        ventana.geometry("400x200")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        tk.Label(
            ventana,
            text="Eliminar Producto",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=20)
        
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=40, pady=10)
        
        tk.Label(form_frame, text="Seleccione producto:", font=("Arial", 10), bg=self.bg_color).pack(pady=5)
        
        combo_productos = ttk.Combobox(
            form_frame,
            values=[p["nombre"] for p in productos],
            font=("Arial", 10),
            width=35,
            state="readonly"
        )
        combo_productos.pack(pady=5)
        
        def eliminar():
            nombre = combo_productos.get()
            
            if not nombre:
                messagebox.showerror("Error", "Debe seleccionar un producto")
                return
            
            respuesta = messagebox.askyesno(
                "Confirmar",
                f"¿Está seguro que desea eliminar '{nombre}'?"
            )
            
            if respuesta:
                if self.inventario.eliminar_producto(nombre):
                    messagebox.showinfo("Éxito", f"Producto '{nombre}' eliminado correctamente")
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto")
        
        btn_frame = tk.Frame(ventana, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Eliminar",
            command=eliminar,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Cancelar",
            command=ventana.destroy,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
    
    def buscar_producto(self):
        """
        Función para buscar un producto específico.
        """
        ventana = tk.Toplevel(self.root)
        ventana.title("Buscar Producto")
        ventana.geometry("400x200")
        ventana.resizable(False, False)
        ventana.configure(bg=self.bg_color)
        
        tk.Label(
            ventana,
            text="Buscar Producto",
            font=("Arial", 14, "bold"),
            bg=self.bg_color
        ).pack(pady=20)
        
        form_frame = tk.Frame(ventana, bg=self.bg_color)
        form_frame.pack(padx=40, pady=10)
        
        tk.Label(form_frame, text="Nombre del producto:", font=("Arial", 10), bg=self.bg_color).pack(pady=5)
        entry_nombre = tk.Entry(form_frame, font=("Arial", 10), width=35)
        entry_nombre.pack(pady=5)
        
        def buscar():
            nombre = entry_nombre.get().strip()
            
            if not nombre:
                messagebox.showerror("Error", "Debe ingresar un nombre")
                return
            
            producto = self.inventario.buscar_producto(nombre)
            
            if producto:
                mensaje = f"Producto encontrado:\n\n"
                mensaje += f"Nombre: {producto['nombre']}\n"
                mensaje += f"Precio: ${producto['precio']:.2f}\n"
                mensaje += f"Cantidad: {producto['cantidad']} unidades\n"
                mensaje += f"Valor Total: ${producto['precio'] * producto['cantidad']:.2f}"
                
                if self.inventario.tiene_stock_bajo(producto['cantidad']):
                    mensaje += f"\n\n⚠️ ALERTA: Stock bajo (mínimo: {self.inventario.stock_minimo})"
                
                messagebox.showinfo("Producto Encontrado", mensaje)
            else:
                messagebox.showwarning("No Encontrado", f"No se encontró ningún producto con el nombre '{nombre}'")
        
        btn_frame = tk.Frame(ventana, bg=self.bg_color)
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="Buscar",
            command=buscar,
            bg=self.button_color,
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Cancelar",
            command=ventana.destroy,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            width=12,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
    
    def stock_bajo(self):
        """
        Función para mostrar productos con stock bajo.
        """
        productos_bajo = self.inventario.obtener_productos_stock_bajo()
        
        if not productos_bajo:
            messagebox.showinfo(
                "Stock Adecuado",
                f"Todos los productos tienen stock suficiente (mínimo: {self.inventario.stock_minimo} unidades)"
            )
            return
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Productos con Stock Bajo")
        ventana.geometry("600x400")
        ventana.configure(bg=self.bg_color)
        
        tk.Label(
            ventana,
            text=f"⚠️ Productos con Stock Bajo (<{self.inventario.stock_minimo} unidades)",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg="#e74c3c"
        ).pack(pady=15)
        
        frame = tk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        tree = ttk.Treeview(
            frame,
            columns=("Nombre", "Precio", "Cantidad"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        scrollbar.config(command=tree.yview)
        
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio ($)")
        tree.heading("Cantidad", text="Cantidad")
        
        tree.column("Nombre", width=300)
        tree.column("Precio", width=120, anchor="center")
        tree.column("Cantidad", width=120, anchor="center")
        
        for producto in productos_bajo:
            tree.insert("", tk.END, values=(
                producto["nombre"],
                f"{producto['precio']:.2f}",
                producto["cantidad"]
            ))
        
        tree.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(
            ventana,
            text=f"Total de productos con stock bajo: {len(productos_bajo)}",
            font=("Arial", 10, "bold"),
            bg=self.bg_color
        ).pack(pady=10)
    
    def reporte_inventario(self):
        """
        Función para generar reporte de inventario.
        """
        total_productos = self.inventario.obtener_total_productos()
        total_unidades = self.inventario.obtener_cantidad_total()
        valor_total = self.inventario.obtener_valor_total()
        productos_bajo = len(self.inventario.obtener_productos_stock_bajo())
        
        mensaje = "═══════════════════════════════════\n"
        mensaje += "     REPORTE DE INVENTARIO\n"
        mensaje += "═══════════════════════════════════\n\n"
        mensaje += f"Total de productos: {total_productos}\n"
        mensaje += f"Total de unidades: {total_unidades}\n"
        mensaje += f"Valor total: ${valor_total:.2f}\n"
        mensaje += f"Productos con stock bajo: {productos_bajo}\n"
        
        if total_productos > 0:
            promedio = valor_total / total_productos
            mensaje += f"Valor promedio por producto: ${promedio:.2f}\n"
        
        mensaje += "\n═══════════════════════════════════"
        
        messagebox.showinfo("Reporte de Inventario", mensaje)
    
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
