"""
Comercio. Durante un rato dentro de un juego de mundo abierto. El gamer puede
obtener y perder distintos artefactos.

En su viaje dentro del mundo virtual el personaje comienza con 0 de oro, una
ranura para tener algún artefacto y el valor de dicho artefacto. Y dentro del tiempo
que juega pueden pasarle algunas cosas como:

- Aventurarse dando un par de vueltas ya sea por bosques o montañas donde
en cada vuelta puede encontrar oro perdido.

- Comprar un artefacto. Dicho artefacto se compra en X partes y en diferentes
tiendas. Cada parte puede tener un precio distinto y una vez obtenido el
artefacto se debe obtener su valor. Nota: el valor del nuevo artefacto se
calcula como 40 veces la cantidad de partes que lo componen.

- Trueque. Acá el gamer puede intercambiar su artefacto con otro jugador. Esto
sucede solo si el valor del artefacto del gamer es menor o igual al del otro
jugador.

NOTA: Saber que la partida del gamer durará hasta que no quiera jugar más.
"""

oro = 0
artefacto = ""
valorArtefacto = 0

seguirJugando = True

artefacto = str(input("Ingrese el artefacto: "))
valorArtefacto = int(input("Ingrese el valor del artefacto: "))

while seguirJugando == True:
	print("Opciones:\n\n[1] Aventurarse\n[2] Comprar un artefacto\n[3] Trueque\nOpcion: ",end="")
	ans = int(input())

	if ans == 1:
		cantOro = int(input("Oro encontrado: "))
		oro += cantOro
		print("Tienes ",oro, " de oro.")
	elif ans == 2:
		artefactoCompra = str(input("Ingrese el artefacto que quiere comprar: "))
		partes = int(input("Ingrese las partes en las que se compra el artefacto: "))
		valorCompra = partes*40

		if oro >= valorCompra:
			print("Compraste el artefacto ",artefactoCompra)
			artefacto = artefactoCompra
			valorArtefacto = valorCompra
			oro -= valorCompra
		else:
			print("No tienes suficiente dinero para comprar el artefacto.")

	elif ans == 3:
		artefactoOtroJ = str(input("Ingrese el artefacto del otro jugador: "))
		valorOtroJ = int(input("Ingrese el precio del artefacto del otro jugador: "))

		if valorArtefacto <= valorOtroJ:
			print("Cambiaste el artefacto ",artefacto," por ",artefactoOtroJ)
			artefacto = artefactoOtroJ
			valorArtefacto = valorOtroJ
		else:
			print("El valor de tu artefacto es mayor al del otro jugador.")


	ansSeguir = str(input("Quiere seguir jugando? [si/no]"))

	if ansSeguir == "no":
		seguirJugando = False

print("Artefacto: ",artefacto)
print("Oro: ",oro)
print("Valor artefacto: ",valorArtefacto)