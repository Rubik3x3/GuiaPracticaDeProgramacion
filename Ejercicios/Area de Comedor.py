"""
Área de comedor: Dentro de esta área se quiere hacer un control de la entrada y salida
de productos como carne y verdura que entran una cierta cantidad de días. Dentro de
la funcionalidad se informará cuando se hace una compra, se ingresará el consumo de
comida y si se pudre algún alimento.

Además de realizar las funciones, dichas anteriormente, al finalizar el ingreso
de datos se debe informar la cantidad total, si es que sobro, de comida (carne y
verdura).

Pero también se necesita controlar que en ningún momento se quede sin
alguna comida. En caso de suceder se debe informar emitiendo alertas de que se ha
quedado sin algún tipo de comida y los valores nunca pueden ser negativos (como
mínimo 0).
"""

carne = 0
verdura = 0
seguir = "si"

while seguir == "si":

	ans = int(input("Acciones a realizar:\n[1] Comprar\n[2] Consumir\n[3] Se pudrio un alimento"))

	if ans == 1:
		pass
	elif ans == 2:
		pass
	elif ans == 3:
		pass
	else:
		pass

	