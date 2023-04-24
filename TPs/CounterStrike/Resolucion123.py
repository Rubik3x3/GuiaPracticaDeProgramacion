import os

UNMIN = int(60)

vidaJugador = int(100)
vida = int(100)
armaduraOpn = int(5)
armadura = int(5)
danioOponente = int(40)
dinero = int(500)
caractTer = int(8)
caractPol = int(20)
equipo = str("h")
arma = int(0)

#-------------PUNTO 1----------------
equipo = str(input("Seleccione un bando: t o p "))
while equipo != "t" and equipo != "p":
	print("")
	print("OPCION INCORRECTA")
	equipo = str(input("Seleccione un bando: t o p "))

if equipo == "t":
	armaduraOpn = armadura + caractPol
	print("Terrorist modelado")
elif equipo == "p":
	danioOponente = danioOponente + caractTer
	armadura += caractPol #armadura = armadura + caractPol
	print("Police modelado")
else:
	print("opcion es incorrecta.")

#----------------PUNTO 2-------------------
arma = int(input("Seleccione el arma: 1- M4A1 ; 2- AUG ; 3 SCOUT"))
while (arma != 1) and (arma != 2) and (arma != 3):
	print("")
	print("OPCION INCORRECTA")
	arma = int(input("Seleccione el arma: 1- M4A1 ; 2- AUG ; 3 SCOUT"))

if arma == 1:
	danioDisparo = int(20)
	balasSegundo = int(8)
elif arma == 2:
	danioDisparo = int(15)
	balasSegundo = int(5)
elif arma == 3:
	danioDisparo = int(45)
	balasSegundo = int(2)

danio = danioDisparo * balasSegundo
if equipo == "t":
	danio += caractTer

danioMinuto = danio * UNMIN
balasMinuto = balasSegundo * UNMIN

print("El danio personal es: ", danio)
print("El danio por minuto es: ", danioMinuto)
print("Las balas por minuto es: ", balasMinuto)

#------------------PUNTO 3-----------------
contOponentCaido = int(0)#contador de cuantos oponentes mato
personaje = str("vivo")
while personaje == "vivo":#sirve para controlar cuando termina la ronda. Sucede cuando el personaje muere
	
	accion = int(input("Accion que lo afecta: 1- dispararOponente; 2-leDisparan ; 3-RescatarTomarRehen; 4 construir trrinchera"))
	while accion != 1 and accion != 2 and accion != 3 and accion != 4:#controla que no ingrese una opcion incorrecta, de ser asi repite 
		print("")
		print("OPCION INCORRECTA")
		accion = int(input("Accion que lo afecta: 1- dispararOponente; 2-leDisparan ; 3-RescatarTomarRehen; 4 construir trrinchera"))
	
	if accion == 1:
		vidaArmadura = vida + armaduraOpn
		if vidaArmadura < danio:
			contOponentCaido += 1
			vidaJugador += 10
			if vidaJugador > 100:
				vidaJugador = int(100)#esta instruiccion hace que la vida sea como maximo 100.
			dinero += 300
		print("Nuestra vida: ", vidaJugador)
	elif accion == 2:
		vidaJugador = vidaJugador - (danioOponente - armadura) 
		if vidaJugador <= 0:
			personaje = str("muere") #cambia el valor del personaje a muerto si se cumple la condicion
			print("has caido. Ronda terminada")
			vidaJugador = int(0)#esta instruccion hace que la vida nunca sea menor a 0 en el caso de que muera
		print("Nuestra vida: ", vidaJugador)
	elif accion == 3:# aca no hace falta contemplar si es police o terror ya que la accion es la misma para ambos
		dinero += 500
		print("Nuestra vida: ", vidaJugador)
	elif accion == 4:
		cantCostales = int(0)
		cantViajes = int(0)

		while cantCostales < 30:
			costalesLlevados = int(input("Ingrese cantidad de costales"))
			cantCostales += costalesLlevados # contCostales = cantCostales + costalesLlevados
			cantViajes += 1

		cantCostales -= 30
		print("Sobro: ", cantCostales)
		print("viajes: ", cantViajes)
		print("Construido")
		print("Nuestra vida: ", vidaJugador)
	else:
		print("Opcion incorrecta")

print("Nuestro dinero es: ", dinero)
print("Matamos a", contOponentCaido, "oponentes")

os.system("pause")