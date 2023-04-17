#TERMINADO

"""
Modelando personajes. Dentro de este programa podremos crear personajes que
luego usaremos en el juego. En principio hay que saber que el usuario puede crear la
cantidad de personajes que quiera antes de hacer otra cosa.

Para crear un personaje se deberá elegir que partes del mismo se quiere
agregar o que parte modificar. Dichas categorías son:

 Pelo: rubio, castaño, blanco, o colorido.
 Ojos: celeste, verde, marrón, blanco.
 Ropa: sin ropa, ropa ligera o armadura.
 Altura: ingresada por el usuario.
 Complexión: delgada, musculosa o normal.

Una vez que se haya seleccionado todo y no se quiera modificar nada, se le
deberá mostrar el personaje armado.
"""
import os

mensaje = "Ningún mensaje"
cantidadPersonajes = 0
personajes=[]

class personaje():
	nombre = ""
	pelo = ""
	ojos = ""
	ropa = ""
	altura = 0
	complexion = ""

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def guardarPersonaje(personaje):
	personajes.append(personaje)

def cambiarPelo(personaje):
	clear()
	print("Ingrese el pelo del personaje:\n[1] Rubio\n[2] Castaño\n[3] Blanco\n[4] Colorido\n")
	nPelo = int(input())
	if nPelo == 1:
		personaje.pelo = "Rubio"
	elif nPelo == 2:
		personaje.pelo = "Castaño"
	elif nPelo == 3:
		personaje.pelo = "Blanco"
	elif nPelo == 4:
		personaje.pelo = "Colorido"
	else:
		print("Ingrese un pelo válido")
		cambiarPelo(personaje)

def cambiarOjos(personaje):
	clear()
	print("Ingrese el pelo del personaje:\n[1] Celeste\n[2] Verde\n[3] Marrón\n[4] Blanco\n")
	nOjos = int(input())
	if nOjos == 1:
		personaje.ojos = "Celeste"
	elif nOjos == 2:
		personaje.ojos = "Verde"
	elif nOjos == 3:
		personaje.ojos = "Marrón"
	elif nOjos == 4:
		personaje.ojos = "Blanco"
	else:
		print("Ingrese unos ojos válidos")
		cambiarOjos(personaje)

def cambiarRopa(personaje):
	clear()
	print("Ingrese la ropa del personaje:\n[1] Sin ropa\n[2] Ropa ligera\n[3] Armadura\n")
	nRopa = int(input())
	if nRopa == 1:
		personaje.ropa = "Sin ropa"
	elif nRopa == 2:
		personaje.ropa = "Ropa ligera"
	elif nRopa == 3:
		personaje.ropa = "Armadura"
	else:
		print("Ingrese una ropa válida")
		cambiarRopa(personaje)

def cambiarAltura(personaje):
	clear()
	print("Ingrese la altura del personaje en centímetros:\n")
	nH = float(input())
	personaje.altura = nH

def cambiarComplexion(personaje):
	clear()
	print("Ingrese la complexion del personaje:\n[1] Delgada\n[2] Musculosa\n[3] Normal")
	nCompl = int(input())
	if nCompl == 1:
		personaje.complexion = "Delgada"
	elif nCompl == 2:
		personaje.complexion = "Musculosa"
	elif nCompl == 3:
		personaje.complexion = "Normal"
	else:
		print("Ingrese una complexion válida")
		cambiarComplexion(personaje)

def crearPersonaje():
	clear()
	print("[CREAR PERSONAJE]\n")
	p = personaje()
	p.nombre = str(input("Ingrese el nombre del personaje:\n"))
	cambiarPelo(p)
	cambiarOjos(p)
	cambiarRopa(p)
	cambiarAltura(p)
	cambiarComplexion(p)
	print("[PERSONAJE CREADO]\nNombre: ",p.nombre,"\nPelo: ",p.pelo,"\nOjos: ",p.ojos,"\nRopa: ",p.ropa,"\nAltura: ",p.altura,"\nComplexión: ",p.complexion)

	ans = str(input("Deseas guardar el personaje? [y/n]"))

	if ans == "y":
		guardarPersonaje(p)
		mainMenu()
	else:
		mainMenu()
def verPersonajes():
	clear()
	print("[LISTA DE PERSONAJES]\n")
	cuenta = 0
	for i in enumerate(personajes):
		print("[",cuenta+1,"]",personajes[cuenta].nombre)
		cuenta += 1
	ans = int(input("\n¿Qué personaje quiere ver?"))
	p = personajes[ans-1]
	print("[PERSONAJE ",p.nombre,"]\nNombre: ",p.nombre,"\nPelo: ",p.pelo,"\nOjos: ",p.ojos,"\nRopa: ",p.ropa,"\nAltura: ",p.altura,"\nComplexión: ",p.complexion)
	ans = str(input("Deseas volver al menu? [y/n]"))
	if ans == "y":
		mainMenu()
	else:
		verPersonajes()
def mainMenu():
	clear()
	global mensaje
	print("[MODELANDO PERSONAJES] [ ",mensaje," ]\n")
	print("Opciones:\n[1] Crear personaje\n[2] Ver mis personajes\n[3] Salir\n",end="")
	ans = int(input())

	if ans == 1:
		crearPersonaje()
	elif ans == 2:
		verPersonajes()
	elif ans == 3:
		print("Saliste del programa.")
		exit()
	else:
		mensaje = "Error, opción inválida"
		mainMenu()
mainMenu()

	
