"""55. Se muestra una lista de 3 productos con el precio correspondiente a cada uno.
También se cuenta con un dinero inicial. El usuario debe poder comprar tantos
productos según quiera o hasta que se quede sin dinero. Luego, el programa debe
decirme el dinero restante y la cantidad de productos comprados. (Realizado por
Leandro Rizzi y Sebastián Powter 3ro 1ra -2019)"""

listaProductos=["Producto 1","Producto 2","Producto 3"]
cantidadProductos=[0,0,0]
precioProductos=[100,200,300]

def listaProductosComprados():
	print("Cantidad de productos comprados:\n")
	for i in range(3):
		print(listaProductos[i],": ",cantidadProductos[i])

def productoAComprar(producto,dinero):
	if dinero >= precioProductos[producto-1]:
		cantidadProductos[producto-1] += 1
		dinero -= precioProductos[producto-1]
		print("\nCompraste el producto: ",listaProductos[producto-1],"\nDinero restante: ",dinero,"\n")
		listaProductosComprados()
		comprar(dinero)
	else:
		insuficienteDinero(dinero)
		
def insuficienteDinero(dinero):			
	print("\nNo tienes suficiente dinero para comprar el producto.\nTe faltan",precioProductos[producto-1]-dinero,"\n")
	listaProductosComprados()
	opcion=str(input("\n¿Desea ingresar más dinero? [SI/NO]\n"))
	if opcion == "SI":
		ingresarDinero(dinero)
	elif opcion == "NO":
		print("\nOk, saliste del programa.")
		exit()
	else:
		print("\nIngrese una opción válida.")

def comprarProducto(dinero):
	producto=int(input("\nIngrese el producto que quiere comprar [1/2/3]:\n"))

	if producto == 1:
		productoAComprar(1,dinero)
	elif producto == 2:
		productoAComprar(2,dinero)
	elif producto == 3:
		productoAComprar(3,dinero)

def salir():
	respuesta=str(input("¿Quiere salir del programa? [SI/NO]"))
	if respuesta == "SI":
		print("Saliste del programa.")
		exit()
	elif respuesta == "NO":
		print("No saliste del programa.")
		comprar()
	else:
		print("Ingrese una opción válida.")
		salir()

def comprar(dinero):
	opcion=str(input("¿Quiere comprar un producto? [SI/NO]"))
	if opcion == "SI":
		comprarProducto(dinero)
	elif opcion == "NO":
		salir()
	else:
		print("Ingrese una opción válida.")
		comprar(dinero)

def ingresarDinero(dinero):
	dineroIngresado = float(input("\nIngrese la cantidad de dinero que quiere ingresar:\n"))
	dinero += dineroIngresado
	print("Ingresaste: $",dineroIngresado,"\nTienes en total: $",dinero)
	comprar(dinero)

def main():
	print("Lista de productos:\n")
	for i in range(3):
		print("[",i+1,"] ",listaProductos[i],": $",precioProductos[i])

	dinero=float(input("\nIngrese su dinero:\n"))
	comprar(dinero)
main()