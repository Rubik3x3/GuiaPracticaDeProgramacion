#TERMINADO

"""
Controles de presión. Dentro del laboratorio se manejan tanques de gases que se
encuentran a determinada presión para a este controlado. En este módulo se deberá
controlar los distintos valores que registra, por hora, un operario. Este podrá registrar
las horas que quiera así que de ante mano no sabemos la cantidad de registros.

 Si la presión es mayor a 70 se debe generar un “ALERTA de explosión”
 si la presión esta entre 25 y 70 inclusive, todo está normal.
 Si la presión es menor a 25, le pedirá al operario que vaya ingresando
comandos (cantidad de puntos de presión) para que vaya aumentando dicha
presión y así encontrarse normal.
"""

presiones=[]
parar = False
cuenta = 0

def mostrarPresiones():
	cuentaP = 0
	for i in enumerate(presiones):
		print("Presion en la hora ",cuentaP+1,": ",presiones[cuentaP]," ( ",verPresRet(presiones[cuentaP])," )")
		cuentaP += 1

def ingresarComandos(presion):
	print("La presión está por debajo de lo normal (",presion,")")
	aumentar = float(input("Ingrese la cantidad de puntos de presion que desea aumentar: "))
	presion = presion + aumentar
	print("La presión esta en: ",presion)
	if presion >= 25:
		print("La presión está normal.")
	else:
		ingresarComandos(presion)

def verPresRet(presion):
	if presion >= 70:
		return "ALERTA de explosión"
	else:
		return "Todo está normal"

def verificarPresion(presion):
	if presion >= 70:
		print("ALERTA de explosión")
	elif presion >= 25 and presion <= 70:
		print("Todo está normal")
	else:
		ingresarComandos(presion)

print("Programa iniciado.")

while parar == False:
	if cuenta != 0:
		ans = str(input("Desea finalizar el programa? [y/n]"))
		if ans == "y":
			parar = True
			break
		else:
			pass
	else:
		pass
	print("Ingrese la presion en la hora ",cuenta+1,": ",end="")
	iPresion = int(input())
	verificarPresion(iPresion)
	presiones.append(iPresion)	
	cuenta += 1

mostrarPresiones()