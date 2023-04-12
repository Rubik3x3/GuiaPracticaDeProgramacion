"""
Simulación de ataques. Dentro de una partida el personaje se enfrenta a un enemigo.
La vida y armadura (de 10 a 30) del enemigo y el daño que hace su personaje es
ingresado por el usuario. El gamer puede elegir entre algunos tipos de ataques hasta
que el oponente cae.
 Ataque múltiple perforante. El gamer elige la cantidad de ataques juntos que
le hace al enemigo. El daño que se le hace no contemplará su armadura
 Ataque básico. Tener en cuenta que al daño que hace el personaje se le
descuenta la armadura del oponente.

 Ataque múltiple especial. El gamer elige la cantidad de ataques juntos que le
hace al enemigo. Pero solo se le efectuará ese daño cuando su armadura sea
distinta a 20.
"""

vidaEnemigo = int(input("Ingrese la vida del enemigo [10-30]: "))
armaduraEnemigo = int(input("Ingrese la armadura del enemigo [10-30]: "))
danioPeronaje = int(input("Ingrese el daño que hace su personaje: "))

ans = int(input("Ataques:\n[1] Ataque múltiple perforante\n[2] Ataque básico\n[3] Ataque múltiple especial\nAtaque: "))

def ataqueMultPerf():
	pass

def ataqueBasico():
	pass

def ataqueMultEsp():
	pass

if ans == 1:
	pass
elif ans == 2:
	pass
elif ans == 3:
	pass

