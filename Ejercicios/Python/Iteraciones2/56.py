"""Mesa de entrada: en este módulo se necesita hacer un control de los empleados que
ingresan y salen de la organización. El módulo estará en una aplicación que la
manejará el recepcionista de la mesa de entrada.

Se deberá controlar la salida y entrada de los empleados en el horario de
07:00hs a 15:00hs, informando cuantos salen o entran en cada hora. Luego el
programa deberá decirme cuantos empleados hay a medida que pasa cada hora, como
así el total de empleados en toda la organización"""

import os

totalEmpleados = 0
empleadosEnLaOrganizacion = 0

empleadosPorHora=[0,0,0,0,0,0,0,0,0]
salen=[0,0,0,0,0,0,0,0,0]
entran=[0,0,0,0,0,0,0,0,0]
horas=["7:00hs","8:00hs","9:00hs","10:00hs","11:00hs","12:00hs","13:00hs","14:00hs","15:00hs",]

for i in range(9):
	os.system("cls")
	print("\nIngrese la cantidad de empleados que entran en la hora: ",horas[i],"\n")
	iEntran=int(input())
	print("\nIngrese la cantidad de empleados que salen en la hora: ",horas[i],"\n")
	iSalen= int(input())

	salen[i] = iSalen
	entran[i] = iEntran

	empleadosEnLaOrganizacion += (entran[i]-salen[i])
	empleadosPorHora[i] = empleadosEnLaOrganizacion

	totalEmpleados += entran[i]

	print("\nEmpleados en la organizacion: ",empleadosEnLaOrganizacion)
	print("En la hora ",horas[i],":\nEntran: ",entran[i],"\nSalen: ",salen[i])

os.system("cls")

for i in range(8):
	print("\nA las ",horas[i]," entran ",entran[i]," empleados y salen ",salen[i])
	print("Empleados en la organizacion: ",empleadosPorHora[i])
	print("Empleados totales de la organizacion: ",totalEmpleados)