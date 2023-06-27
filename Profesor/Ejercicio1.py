"""
Solicitar el ingreso de la compra de 4 productos con su precio y cantidad.
Visualizar los datos ingresados por el usuario.
Calcular el importe total de la compra de los cuatro artículos sabiendo 
que si el importe total es superior a 2000 se le efectua un descuento del 10%
y si es superior a 3000 se le efectua un descuento del 20%.
"""

listaProductos = []

for i in range(4):
	producto = []
	nombre = str(input("Producto: "))
	producto.append(nombre)
	precio = int(input("Precio: "))
	producto.append(precio)
	cantidad = int(input("Cantidad: "))
	producto.append(cantidad)
	listaProductos.append(producto)

print(listaProductos)