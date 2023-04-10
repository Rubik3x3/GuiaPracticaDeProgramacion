#Franco Talarico 3°1

"""
En un almacén se implementa un sistema que aplica determinados descuentos con distintas
condiciones.

Cuando se atiende a un cliente se le pide al cliente el DNI y la edad.
Luego el tipo de producto, cantidad y precio. Máximo podrá comprar 3 tipos de productos
distintos, pero saber que puede comprar menos.
Primeros descuentos:

-En principio y como prioridad se les aplicara un descuento a los jubilados (mayores de 65 años) del 30%
-Luego, en caso de no ser jubilado, se evaluará si su DNI es impar. EN caso de ser cierto se le
aplicara un descuento del 15%
Segundos descuentos:
-Por último, se le aplicara un descuento del 10%, a todos los clientes, cuando el monto de la compra
esté entre los 2500 y 5000 pesos.

Al final informar monto total y vuelto al cliente
"""

dni=int(input("Ingrese el número de DNI: "))
edad=int(input("Ingrese su edad en años: "))

comprar = True

cantTipoProducto = 0

porcDescuento = 0
porcDescuento2 = 0

precioFinal = 0

def comprarProducto():
	global comprar,precioFinal,cantTipoProducto
	while comprar == True:
		if cantTipoProducto < 3:
			tipoP=str(input("Ingrese el tipo de producto: "))
			cantP=int(input("Ingrese la cantidad: "))
			precio=int(input("Ingrese el precio del producto: "))

			precioFinal += cantP*precio

			print("Precio ",tipoP,": $",cantP*precio)

			ans=str(input("¿Quiere comprar otro producto? [y/n]"))

			if ans == "n":
				comprar = False
		else:
			comprar = False

		cantTipoProducto+=1

def applDesc():
	global edad,porcDescuento,precioFinal
	if edad >= 65:
		porcDescuento = 30
	else:
		if dni % 2 != 0:
			porcDescuento = 15
		else:
			pass
	precioFinal -= (precioFinal*porcDescuento)/100

def applDesc2():
	global precioFinal,porcDescuento2
	if precioFinal >= 2500 and precioFinal <= 5000:
		porcDescuento2 = 10
	precioFinal -= (precioFinal*porcDescuento2)/100

def mostDatosYVuelto():
	global precioFinal
	print("Precio Total: $",precioFinal)
	monto=int(input("¿Con cuanto va a pagar?: "))
	vuelto = monto - precioFinal
	print("Tu vuelto es de $",vuelto)

comprarProducto()
applDesc()
applDesc2()

mostDatosYVuelto()