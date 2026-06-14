"""
Sistema de Gestión de una Tienda de Videojuegos
Ejercicio Integrador - Módulo 3 (Python)

Aplica: variables, condicionales, ciclos, funciones y colecciones (listas y diccionarios).
"""

# ===================================================================
#  DATOS INICIALES
# ===================================================================

videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

# Reto opcional: historial de ventas
historial_ventas = []


# ===================================================================
#  FUNCIONES AUXILIARES DE ENTRADA (validación robusta)
# ===================================================================

def leer_texto(mensaje):
    """Lee texto no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  El valor no puede estar vacío. Intente de nuevo.")


def leer_entero(mensaje, minimo=None):
    """Lee un entero. Si se indica 'minimo', el valor debe ser >= minimo."""
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero válido.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  El valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def leer_flotante(mensaje, minimo=None):
    """Lee un número (acepta decimales). Si se indica 'minimo', debe ser >= minimo."""
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número válido.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  El valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


# ===================================================================
#  REQUISITOS FUNCIONALES
# ===================================================================

def agregar_videojuego(videojuegos):
    """4.1 Agrega un videojuego al inventario con validaciones."""
    print("\n--- Agregar videojuego ---")

    codigo = leer_texto("Ingrese el código: ").upper()
    if codigo in videojuegos:
        print(f"  El código '{codigo}' ya existe. No se puede repetir.")
        return

    nombre = leer_texto("Ingrese el nombre: ")
    plataforma = leer_texto("Ingrese la plataforma (PC, PlayStation, Xbox, Nintendo): ")
    precio = leer_flotante("Ingrese el precio: ", minimo=1)      # mayor que cero
    cantidad = leer_entero("Ingrese la cantidad: ", minimo=1)     # mayor que cero

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }
    print(f"  Videojuego '{nombre}' agregado correctamente.")


def mostrar_inventario(videojuegos):
    """4.2 Recorre el diccionario e imprime todos los videojuegos."""
    print("\n--- Inventario ---")
    if not videojuegos:
        print("  No hay videojuegos registrados.")
        return

    print(f"{'Código':<8}{'Nombre':<30}{'Plataforma':<18}{'Precio':>12}{'Cant.':>8}")
    print("-" * 76)
    for codigo, datos in videojuegos.items():
        print(f"{codigo:<8}{datos['nombre']:<30}{datos['plataforma']:<18}"
              f"${datos['precio']:>11,.0f}{datos['cantidad']:>8}")


def buscar_videojuego(videojuegos):
    """4.3 Busca un videojuego por código y muestra su información."""
    print("\n--- Buscar videojuego ---")
    codigo = leer_texto("Ingrese el código a buscar: ").upper()

    if codigo in videojuegos:
        datos = videojuegos[codigo]
        print(f"\n  Código:     {codigo}")
        print(f"  Nombre:     {datos['nombre']}")
        print(f"  Plataforma: {datos['plataforma']}")
        print(f"  Precio:     ${datos['precio']:,.0f}")
        print(f"  Cantidad:   {datos['cantidad']}")
    else:
        print(f"  No existe ningún videojuego con el código '{codigo}'.")


def actualizar_precio(videojuegos):
    """4.4 Modifica el precio de un videojuego existente."""
    print("\n--- Actualizar precio ---")
    codigo = leer_texto("Ingrese el código: ").upper()

    if codigo not in videojuegos:
        print(f"  No existe el videojuego '{codigo}'.")
        return

    actual = videojuegos[codigo]['precio']
    print(f"  Precio actual: ${actual:,.0f}")
    nuevo = leer_flotante("Ingrese el nuevo precio: ", minimo=1)
    videojuegos[codigo]['precio'] = nuevo
    print(f"  Precio actualizado a ${nuevo:,.0f}.")


def registrar_venta(videojuegos):
    """4.5 Registra una venta, descuenta inventario y muestra la factura."""
    print("\n--- Registrar venta ---")
    codigo = leer_texto("Ingrese código del videojuego: ").upper()

    if codigo not in videojuegos:
        print(f"  No existe el videojuego '{codigo}'.")
        return

    juego = videojuegos[codigo]
    cantidad = leer_entero("Ingrese cantidad a vender: ", minimo=1)

    if cantidad > juego['cantidad']:
        print(f"  Inventario insuficiente. Disponibles: {juego['cantidad']}.")
        return

    # Cálculos
    total = juego['precio'] * cantidad

    # Reto opcional: descuento del 10% en ventas mayores a $500.000
    descuento = 0
    if total > 500000:
        descuento = total * 0.10
        total -= descuento

    # Descontar inventario
    juego['cantidad'] -= cantidad

    # Guardar en el historial (reto opcional)
    historial_ventas.append({
        "codigo": codigo,
        "nombre": juego['nombre'],
        "cantidad": cantidad,
        "total": total
    })

    # Factura
    print("\nFactura")
    print("-------")
    print(f"Juego: {juego['nombre']}")
    print(f"Precio unitario: ${juego['precio']:,.0f}")
    print(f"Cantidad: {cantidad}")
    if descuento > 0:
        print(f"Descuento (10%): -${descuento:,.0f}")
    print(f"Total: ${total:,.0f}")


def mostrar_estadisticas(videojuegos):
    """4.6 Muestra estadísticas del inventario."""
    print("\n--- Estadísticas ---")
    if not videojuegos:
        print("  No hay videojuegos registrados.")
        return

    total_juegos = len(videojuegos)
    valor_inventario = sum(d['precio'] * d['cantidad'] for d in videojuegos.values())
    promedio = sum(d['precio'] for d in videojuegos.values()) / total_juegos

    # Videojuego más costoso
    cod_caro = max(videojuegos, key=lambda c: videojuegos[c]['precio'])
    # Videojuego con mayor cantidad
    cod_cant = max(videojuegos, key=lambda c: videojuegos[c]['cantidad'])

    print(f"  Total de videojuegos registrados: {total_juegos}")
    print(f"  Valor total del inventario:       ${valor_inventario:,.0f}")
    print(f"  Más costoso:    {videojuegos[cod_caro]['nombre']} "
          f"(${videojuegos[cod_caro]['precio']:,.0f})")
    print(f"  Mayor cantidad: {videojuegos[cod_cant]['nombre']} "
          f"({videojuegos[cod_cant]['cantidad']} unidades)")
    print(f"  Promedio de precios:              ${promedio:,.0f}")

    # Reto opcional: inventario bajo (cantidad menor a 3)
    bajos = [d['nombre'] for d in videojuegos.values() if d['cantidad'] < 3]
    if bajos:
        print(f"  Inventario bajo (< 3): {', '.join(bajos)}")


def eliminar_videojuego(videojuegos):
    """4.7 Elimina un videojuego por su código."""
    print("\n--- Eliminar videojuego ---")
    codigo = leer_texto("Ingrese el código a eliminar: ").upper()

    if codigo in videojuegos:
        nombre = videojuegos[codigo]['nombre']
        confirmar = leer_texto(f"¿Seguro que desea eliminar '{nombre}'? (s/n): ").lower()
        if confirmar == "s":
            del videojuegos[codigo]
            print(f"  Videojuego '{nombre}' eliminado.")
        else:
            print("  Operación cancelada.")
    else:
        print(f"  No existe el videojuego '{codigo}'.")


# ===================================================================
#  MENÚ PRINCIPAL
# ===================================================================

def menu():
    """Muestra el menú y devuelve la opción elegida."""
    print("\n===== TIENDA DE VIDEOJUEGOS =====")
    print("1. Agregar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego por código")
    print("4. Actualizar precio")
    print("5. Registrar venta")
    print("6. Mostrar estadísticas")
    print("7. Eliminar videojuego")
    print("8. Salir")
    return leer_entero("Seleccione una opción: ")


def main():
    """Bucle principal del programa."""
    while True:
        opcion = menu()

        if opcion == 1:
            agregar_videojuego(videojuegos)
        elif opcion == 2:
            mostrar_inventario(videojuegos)
        elif opcion == 3:
            buscar_videojuego(videojuegos)
        elif opcion == 4:
            actualizar_precio(videojuegos)
        elif opcion == 5:
            registrar_venta(videojuegos)
        elif opcion == 6:
            mostrar_estadisticas(videojuegos)
        elif opcion == 7:
            eliminar_videojuego(videojuegos)
        elif opcion == 8:
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("  Opción no válida. Elija un número del 1 al 8.")


if __name__ == "__main__":
    main()
