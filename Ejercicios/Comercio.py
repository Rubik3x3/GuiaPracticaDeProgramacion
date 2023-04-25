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
		pass
	elif ans == 3:
		pass

	ansSeguir = str(input("Quiere seguir jugando? [si/no]"))

	if ansSeguir == "no":
		seguirJugando = False





