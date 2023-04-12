"""Realizar una calculadora con 5 opciones de operación. NOTA: controla que no ingresen
opciones incorrectas. En tal caso volver a ingresar una opción. Como condición se debe
dejar poder realizar otra opción en caso de que el usuario quiera."""


def reiniciarPrograma():
	opcion=str(input("¿Quiere realizar otra operación? [SI/NO]"))
	if opcion == "SI":
		main()
	elif opcion == "NO":
		print("Saliste del programa.")
		exit()
	else:
		print("Ingrese una opción válida.")
		reiniciarPrograma

def mostrarResultado(num1,num2,operacion,resultado):
	print("RESULTADO: ",num1," ",operacion," ",num2," = ",resultado)
	reiniciarPrograma()

def sumar():
	a = float(input("Ingrese el número 1 de la suma:\n"))
	b = float(input("Ingrese el número 2 de la suma:\n"))

	resultado = a+b
	mostrarResultado(a,b,"/",resultado)

def restar():
	a = float(input("Ingrese el número 1 de la resta:\n"))
	b = float(input("Ingrese el número 2 de la reta:\n"))

	resultado = a-b
	mostrarResultado(a,b,"/",resultado)

def multiplicar():
	a = float(input("Ingrese el número 1 de la multiplicación:\n"))
	b = float(input("Ingrese el número 2 de la multiplicación:\n"))

	resultado = a*b
	mostrarResultado(a,b,"/",resultado)

def dividir():
	a = float(input("Ingrese el número 1 de la división:\n"))
	b = float(input("Ingrese el número 2 de la división:\n"))

	resultado = a/b
	mostrarResultado(a,b,"/",resultado)

def potencia():
	a = float(input("Ingrese el número 1 de la potencia:\n"))
	b = float(input("Ingrese el número 2 de la potencia:\n"))

	resultado = a**b
	mostrarResultado(a,b,"elevado a la",resultado)

def main():
	opcion=input("Ingrese una operación:\n[1] Sumar\n[2] Restar\n[3] Multiplicar\n[4] Dividir\n[5] Potencia\n")
	
	if int(opcion) == 1:
		print("Opcion seleccionada: SUMA")
		sumar()
	elif int(opcion) == 2:
		print("Opcion seleccionada: RESTA")
		restar()
	elif int(opcion) == 3:
		print("Opcion seleccionada: MUTIPLICACIÓN")
		multiplicar()
	elif int(opcion) == 4:
		print("Opcion seleccionada: DIVISIÓN")
		dividir()
	elif int(opcion) == 5:
		print("Opcion seleccionada: POTENCIA")
		potencia()
	else:
		print("\n[Error, ingrese una opción posible.]\n")
		main()

print("[CALCULADORA]")
main()
