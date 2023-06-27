"""
Escribir un programa que pida al usuario una palabra
y muestre por pantalla el numero de veces que contiene cada vocal.
"""

# A E I O U OTRAS_LETRAS
vocales = ["A","E","I","O","U","NO VOCAL"] 
cantVocales = [0,0,0,0,0,0]

palabra = str(input("Ingrese una palabra:\n"))

for letra in palabra:
	if letra.upper() == "A":
		cantVocales[0] += 1
	elif letra.upper() == "E":
		cantVocales[1] += 1
	elif letra.upper() == "I":
		cantVocales[2] += 1
	elif letra.upper() == "O":
		cantVocales[3] += 1
	elif letra.upper() == "U":
		cantVocales[4] += 1
	else:
		cantVocales[5] += 1

cont = int(0)

for i in vocales:
	print(f'Letra {i}: ',cantVocales[cont])
	cont += 1