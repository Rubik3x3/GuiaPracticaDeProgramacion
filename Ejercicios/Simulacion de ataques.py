"""
Simulación de ataques. Dentro de una partida el personaje se enfrenta a un enemigo.

La vida y armadura (de 10 a 30) del enemigo y el daño que hace su personaje es
ingresado por el usuario. El gamer puede elegir entre algunos tipos de ataques hasta
que el oponente cae.

-- Ataque múltiple perforante. El gamer elige la cantidad de ataques juntos que
le hace al enemigo. El daño que se le hace no contemplará su armadura

-- Ataque básico. Tener en cuenta que al daño que hace el personaje se le
descuenta la armadura del oponente.

-- Ataque múltiple especial. El gamer elige la cantidad de ataques juntos que le
hace al enemigo. Pero solo se le efectuará ese daño cuando su armadura sea
distinta a 20.
"""

danioPersonaje = 0

def ataqueMultPerf(danio):
	ataques=int(input("Ingrese la cantidad de ataques: "))
	danio*=ataques
	return danio

def ataqueBasico(danio,armadura):
	danio -= armadura
	return danio

def ataqueMultEsp(danio,armadura):
	ataques=int(input("Ingrese la cantidad de ataques juntos: "))
	if armadura != 20:
		danio *= ataques
		return danio
	else:
		print("\nLa armadura es igual a 20 y no se puede efectuar el ataque.")

vidaEnemigo = int(input("Ingrese la vida del enemigo [10-30]: "))
armaduraEnemigo = int(input("Ingrese la armadura del enemigo [10-30]: "))
iDanioPersonaje = int(input("Ingrese el daño que hace su personaje: "))

danioPersonaje = iDanioPersonaje

if vidaEnemigo >= 10 and vidaEnemigo <= 30 and armaduraEnemigo >= 10 and armaduraEnemigo <= 30:
		pass
else:
	print("\nIngrese los datos válidos.")
	vidaEnemigo = int(input("Ingrese la vida del enemigo [10-30]: "))
	armaduraEnemigo = int(input("Ingrese la armadura del enemigo [10-30]: "))
	danioPersonaje = int(input("Ingrese el daño que hace su personaje: "))

while vidaEnemigo > 0:
	ans = int(input("\nAtaques:\n[1] Ataque múltiple perforante\n[2] Ataque básico\n[3] Ataque múltiple especial\n\nAtaque: "))
	
	if ans == 1:
		danioPersonaje = ataqueMultPerf(danioPersonaje)
		vidaEnemigo -= danioPersonaje
	elif ans == 2:
		danioPersonaje = ataqueBasico(danioPersonaje,armaduraEnemigo)
		armaduraEnemigo -= danioPersonaje
		if armaduraEnemigo < 0:
			danioPersonaje += armaduraEnemigo
	elif ans == 3:
		ataqueMultEsp(danioPersonaje,armaduraEnemigo)
		armaduraEnemigo -= danioPersonaje
		if armaduraEnemigo < 0:
			danioPersonaje += armaduraEnemigo
	print("\nLa armadura del enemigo es: ",armaduraEnemigo,"La vida del enemigo es: ",vidaEnemigo)
	danioPersonaje = iDanioPersonaje
	
if vidaEnemigo <= 0:
	print("La armadura del enemigo es: ",armaduraEnemigo,"La vida del enemigo es: 0\nEl enemigo murio.")