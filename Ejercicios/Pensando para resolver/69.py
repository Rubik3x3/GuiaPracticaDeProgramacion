#Dado un numero de 5 dígitos decir si es capicúa.
numero=str(input("Ingrese un número: "))

cantNumeros = 0
numeroInv = ""

for i in numero:
	cantNumeros += 1
	numeroInv = str(i)+numeroInv
	
if cantNumeros == 5:
	if int(numeroInv) == int(numero):
		print("El número es capicúa.")
	else:
		print("El número no es capicúa.")
else:
	print("El número no tiene 5 díjitos.")
