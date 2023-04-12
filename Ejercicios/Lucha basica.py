"""
Lucha Básica. El juego será acerca de un luchador que debe vencer a su oponente. Al
luchar, el jugador puede usar dos diferentes ataques, una patada (daño de 15) o un
puñetazo (daño de 10).

La lucha termina cuando terminen las X cantidad de turnos o cuanto el
oponente caiga. La vida del oponente se carga antes de comenzar la lucha. Luego de la
lucha se evaluará:

- Si la vida del oponente llega a una cantidad mayor a -10, pero menor o igual a
0, el jugador ganará.

- Si la vida del oponente llega por debajo de -10, este será dañado de una
forma grave, y el jugador perderá.

- Si la vida del oponente no llega a 0 en menos de X turnos, el jugador perderá.
"""
turnos = 0
turnoActual = 0
vidaOponente = 0

turnos = int(input("Ingrese la cantidad de turnos de la partida: "))
vidaOponente = int(input("Ingrese la vida del oponente: "))

def ataque(danio):
	global vidaOponente
	vidaOponente -= danio

for i in range(turnos):
	turnoActual += 1
	ansAtaque = int(input("\nIngrese el ataque que quiere usar:\n[1] Puñetaso (10 de daño)\n[2] Patada (15 de daño)\n"))

	if ansAtaque == 1:
		ataque(10)
	elif ansAtaque == 2:
		ataque(15)

	if vidaOponente > -10 and vidaOponente <= 0:
		print("El jugador gano.")
		break

	elif vidaOponente < -10:
		print("El oponente fue dañado de forma grave, el jugador perdio.")
		break

	print("Turno: ",i+1,"\nVida del oponente: ",vidaOponente)
	
if turnoActual >= turnos:
	print("El jugador perdio. Se acabaron los turnos.")