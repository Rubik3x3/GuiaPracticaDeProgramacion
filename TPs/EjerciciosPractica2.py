"""
Se nos pide realizar un módulo para un proyecto de gestión académica. Dicho módulo será
usado por el alumno para obtener ciertas estadísticas de su cursada.
En principio el alumno ingresará las notas finales de 3 materias. El programa deberá
decirme:

 Cuantas materias aprobó con poca diferencia. Se aprueba con poca diferencia, con
una nota final entre 6 y 8 inclusive.
 La suma de todas sus notas.
 En caso de aprobar todas las materias decirle que “siga así”. Si no, decirle que intente
dedicarle un poco más de estudio si es que aprobó al menos una materia. En caso de
haber desaprobado todo, decirle que deje el Fornite y las series.
"""

notas = [0.0,0.0,0.0]
sumaN = 0.0
mensaje = ""
aprobadas = 0
aprobadasCPD = 0

def mostrarResultados(cantNotas):
	print("Resultados:\nNotas: ",notas,"\nSuma de las notas: ",sumaN,"\nPromedio: ",sumaN/cantNotas,"\nAprobadas: ",aprobadas,"\nAprobadas con diferencia: ",aprobadasCPD)

def verMensaje():
	if aprobadas == 3:
		print("\nMensaje: Sigue así!")
	elif aprobadas < 3 and aprobadas >= 1:
		print("\nMensaje: Intenta dedicarle un poco más al estudio.")
	else:
		print("\nMensaje: DEJA EL FORNITE Y LAS SERIES!")

def ingresoNotas(cantNotas):
	global sumaN,aprobadas,aprobadasCPD
	for i in range(cantNotas):
		print("Ingrese la nota final número ",i+1)
		nota = float(input())
		sumaN += nota
		notas[i] = nota
		if nota >= 6 and nota <= 8:
			aprobadas += 1
			aprobadasCPD += 1
		elif nota > 8:
			aprobadas += 1

ingresoNotas(3)
mostrarResultados(3)
verMensaje()