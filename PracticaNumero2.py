ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]
def mostrarOpciones():
    print("BIENVENIDOS")
    print(
        """
        1. Mostrar listado de ventas
        2. Agregar producto
        3. Calcular la suma total de las ventas
        4. Calcular el promedio de ventas
        5. Mostrar el producto con más unidades vendidas
        6. Mostrar listado de productos
        7. Salir
    """
    )

def mostrar_ventas():
    print("\nListado de ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {'Sí' if venta['promocion'] else 'No'}")

def añadir_producto():
    fecha = input("Ingrese la fecha (DD-MM-YYYY): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    promocion = input("¿Está en promoción? (sí/no): ").strip().lower() == "sí"
    nueva_venta = {"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion}
    ventas.append(nueva_venta)
    print("Producto añadido exitosamente.")

def calcular_suma_total():
    total = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    print(f"\nLa suma total de las ventas es: {total:.2f}")

def calcular_promedio_ventas():
    total_ventas = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
    cantidad_productos = len(ventas)
    promedio = total_ventas / cantidad_productos if cantidad_productos > 0 else 0
    print(f"\nEl promedio de las ventas es: {promedio:.2f}")

def producto_mas_vendido():
    mas_vendido = max(ventas, key=lambda venta: venta["cantidad"])
    print(f"\nEl producto más vendido es {mas_vendido['producto']} con {mas_vendido['cantidad']} unidades.")

def mostrar_listado_productos():
    productos = {venta["producto"] for venta in ventas}
    print("\nListado de productos:")
    for producto in productos:
        print(producto)

def menu():
    while True:
        mostrarOpciones()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_ventas()
        elif opcion == "2":
            añadir_producto()
        elif opcion == "3":
            calcular_suma_total()
        elif opcion == "4":
            calcular_promedio_ventas()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            mostrar_listado_productos()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el menú
menu()