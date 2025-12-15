def validar_nombre(nombre):
    """
    Valida que el nombre del producto no esté vacío y tenga un formato válido.
    
    Args:
        nombre (str): Nombre del producto a validar
        
    Returns:
        tuple: (bool, str) - (es_valido, mensaje_error)
    """
    if not nombre or nombre.strip() == "":
        return False, "El nombre no puede estar vacío"
    
    if len(nombre.strip()) < 2:
        return False, "El nombre debe tener al menos 2 caracteres"
    
    if len(nombre.strip()) > 50:
        return False, "El nombre no puede exceder 50 caracteres"
    
    return True, ""


def validar_precio(precio_str):
    """
    Valida que el precio sea un número positivo.
    
    Args:
        precio_str (str): Precio como string a validar
        
    Returns:
        tuple: (bool, float/str) - (es_valido, precio_convertido o mensaje_error)
    """
    if not precio_str or precio_str.strip() == "":
        return False, "El precio no puede estar vacío"
    
    try:
        precio = float(precio_str.strip())
        
        if precio < 0:
            return False, "El precio no puede ser negativo"
        
        if precio == 0:
            return False, "El precio debe ser mayor que 0"
        
        if precio > 1000000:
            return False, "El precio no puede exceder 1,000,000"
        
        return True, round(precio, 2)
        
    except ValueError:
        return False, "El precio debe ser un número válido"


def validar_cantidad(cantidad_str):
    """
    Valida que la cantidad sea un número entero no negativo.
    
    Args:
        cantidad_str (str): Cantidad como string a validar
        
    Returns:
        tuple: (bool, int/str) - (es_valido, cantidad_convertida o mensaje_error)
    """
    if not cantidad_str or cantidad_str.strip() == "":
        return False, "La cantidad no puede estar vacía"
    
    try:
        cantidad = int(cantidad_str.strip())
        
        if cantidad < 0:
            return False, "La cantidad no puede ser negativa"
        
        if cantidad > 100000:
            return False, "La cantidad no puede exceder 100,000"
        
        return True, cantidad
        
    except ValueError:
        return False, "La cantidad debe ser un número entero válido"


def formatear_precio(precio):
    """
    Formatea un precio para mostrar con símbolo de moneda.
    
    Args:
        precio (float): Precio a formatear
        
    Returns:
        str: Precio formateado
    """
    return f"${precio:,.2f}"


def formatear_producto(nombre, precio, cantidad):
    """
    Formatea la información de un producto para mostrar.
    
    Args:
        nombre (str): Nombre del producto
        precio (float): Precio del producto
        cantidad (int): Cantidad en stock
        
    Returns:
        str: Información del producto formateada
    """
    return f"{nombre} - {formatear_precio(precio)} - Stock: {cantidad}"
