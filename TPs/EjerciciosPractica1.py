#Franco Talarico 3°1

"""
En el área de RRHH para evaluar postulantes, se hacen entrevistas de 3 personas (postulantes),
que ingresan los datos pedidos a continuación.
El personal de recursos humanos especifica en el programa que puesto se necesita
ocupar, es decir que no lo ingresan por pantalla, ya está establecido, pero en algún momento
puede cambiar.

En principio cada postulante ingresará el puesto que quiere ocupar, su especialidad y
su altura. En base a esos datos el modulo devolverá:
 Cuantos son petisos en dicha entrevista. Será petiza una persona que mida menos de
150cm.

 Si el puesto que quiere ocupar el postulante coincide con el puesto que se necesita
ocupar, entonces se le otorga el trabajo, si no seguirá buscando un nuevo empleado.
 Si al menos un postulante es técnico en computación.
"""

puestoNecesario="catador"

tecComputacion = False
obtuvoPuesto = False

especialidadAprobado = ""

postulantes = 0
postulantesAEntrevistar = 3
petizos = 0

def verPetizos(altura):
	global petizos
	if altura < 150:
		petizos += 1
	else:
		pass

def verEspecialidad(especialidad):
	global tecComputacion
	if especialidad == "tecnico en computacion":
		tecComputacion = True
	else:
		pass

def mostrarDatos(especialidad):
	print("\nDatos de la entrevista:\nPetizos: ",petizos)
	if tecComputacion == True:
		print("Hubo un técnico en computación.")
	else:
		print("No hubo un técnico en computación.")
	if obtuvoPuesto == True:
		print("\nEl especialista en ",especialidad," obtuvo el puesto.")
	else:
		print("\nNinguna persona obtuvo el puesto.")

for i in range(3):
	puesto=str(input("Ingrese el puesto que quiere ocupar: "))
	especialidad=str(input("Ingrese su especialidad: "))
	altura=int(input("Ingrese su altura en centímetros: "))

	especialidadAprobado = especialidad

	verPetizos(altura)
	verEspecialidad(especialidad)

	if puesto == puestoNecesario:
		print("\nConseguiste el empleo.")
		obtuvoPuesto = True
		break
	else:
		print("\nNo conseguiste el empleo.")

mostrarDatos(especialidadAprobado)