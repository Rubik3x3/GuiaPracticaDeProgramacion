fuerza = 0
edad = 0
armadura = 0
honestidad = False
nombre = ""
def mostrarDatos():
	print("Nombre: ",nombre,"\nEdad: ",edad,"\nFuerza: ",fuerza,"\nArmadura: ",armadura,"\nHonestidad: ",honestidad)
def selGema():
	global nombre,fuerza,edad,honestidad,armadura
	mostrarDatos()
	ans = int(input("\n¿Qué gema usar? \n[1] Gema del poder\n[2] Gema de la realidad\n[3] Gema del alma\n"))
	if ans == 1:
		armadura -= 50
		if armadura < 0:
			armadura = 0
		else:
			pass
		mostrarDatos()
	elif ans == 2:
		nombre = "Peter la anguila"
		edad = 20
		mostrarDatos()
	elif ans == 3:
		if fuerza < 100:
			fuerza *= 2
			honestidad = False
		elif fuerza > 100 and fuerza < 200:
			fuerza /= 3
			honestidad = True
		else:
			print("Mejor no molestar a este fortachón.")
def selEnemigo():
	global nombre,fuerza,edad,honestidad,armadura
	ans = str(input("\n¿Contra quien se enfrentará Thanos? [StarLord/IronMan]: "))
	if ans == "StarLord":
		nombre = "StarLord"
		fuerza = 70
		edad = 38
		honestidad = True
		armadura = 20
	elif ans == "IronMan":
		nombre = "IronMan"
		fuerza = 160
		honestidad = 52
		honestidad = False
		armadura = 90
	else:
		print("Opción Inválida.")
	selGema()
selEnemigo()