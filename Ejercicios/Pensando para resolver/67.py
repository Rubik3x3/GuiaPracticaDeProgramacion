#Dado un numero decir si dicho número es primo.

numero=int(input("Ingrese un número para ver si es primo: "))
divisores=[]

if numero > 0:

	for i in range(1,numero+1):
		if numero % i == 0:
			divisores.append(int(i))

	if divisores[1] == numero :
		print("El número ",numero," es primo.",sep="")
	else:
		print("El número ",numero," no es primo.",sep="")

	print("Los divisores de ",numero," son: ",divisores)
else:
	print("Ingrese un número mayor a 0.")