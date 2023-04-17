#TERMINADO

"""
Acción PvP. El módulo que debemos desarrollar es para un juego donde una partida
tiene varias rondas. Al comenzar la partida el personaje cuenta con 100 de vida
En cada ronda puede pasar:
- Matar oponente. Lo que hace es recuperar 10 de vida
- Recibe ataque. Acá pierde 40 de vida.
La partida termina una vez que el personaje muere. Cada vez que termina la
ronda hay que mostrarle al usuario la vida. Y cuando termino la partida hay que decirle
cuantos oponentes mató.
"""

import os

vidaPersonaje = 100
oponentesMuertos = 0
ronda = 1

def matarOponente(vida,recuperar,oponentes):
	print("\nEl personaje mato a un oponente y recupero ",recuperar, " de vida.\n")
	datos = [0,0]
	datos[0] = vida + recuperar
	datos[1] = oponentes + 1

	return datos

def recibirAtaque(vida,danio):
	print("\nEl personaje recibio ",danio, " de daño.\n")
	return vida - danio

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

clear()

while vidaPersonaje > 0:
	print("Acción Pvp - Ronda: ",ronda,"\nVida: ",vidaPersonaje,"\n")
	ans = int(input("Acciones:\n[1] Matar oponente\n[2] Recibe ataque\n"))
	if ans == 1:
		datos = matarOponente(vidaPersonaje,10,oponentesMuertos)

		vidaPersonaje = datos[0]
		oponentesMuertos = datos[1]
	elif ans == 2:
		vidaPersonaje = recibirAtaque(vidaPersonaje,40)
	ronda += 1

clear()
print("El personaje murio.\nMataste a ",oponentesMuertos," oponentes\nRondas: ",ronda-1,sep="")


