def mostrar_menu():
    """
    Muestra el menú principal del sistema de gestión de stock.
    """
    print("\n" + "="*50)
    print(" "*10 + "SISTEMA DE GESTIÓN DE STOCK")
    print("="*50)
    print("\n[1] Agregar producto")
    print("[2] Actualizar stock")
    print("[3] Eliminar producto")
    print("[4] Buscar producto")
    print("[5] Listar todos los productos")
    print("[6] Productos con stock bajo")
    print("[7] Reporte de inventario")
    print("[8] Salir")
    print("\n" + "-"*50)


def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción (1-8): ").strip()
            
            if opcion == "1":
                print("\n✓ Opción 'Agregar producto' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "2":
                print("\n✓ Opción 'Actualizar stock' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "3":
                print("\n✓ Opción 'Eliminar producto' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "4":
                print("\n✓ Opción 'Buscar producto' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "5":
                print("\n✓ Opción 'Listar todos los productos' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "6":
                print("\n✓ Opción 'Productos con stock bajo' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "7":
                print("\n✓ Opción 'Reporte de inventario' seleccionada")
                print("(Funcionalidad pendiente de implementación)")
                input("\nPresione Enter para continuar...")
                
            elif opcion == "8":
                print("\n" + "="*50)
                print(" "*8 + "Gracias por usar el sistema")
                print("="*50)
                print("\n¡Hasta pronto!\n")
                break
                
            else:
                print("\n❌ ERROR: Opción inválida.")
                print("Por favor, seleccione un número entre 1 y 8.")
                input("\nPresione Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n" + "="*50)
            print(" "*12 + "Programa interrumpido")
            print("="*50)
            print("\n¡Hasta pronto!\n")
            break
            
        except Exception as e:
            print(f"\n❌ ERROR inesperado: {e}")
            print("Por favor, intente nuevamente.")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    print("\n¡Bienvenido al Sistema de Gestión de Stock!\n")
    main()
