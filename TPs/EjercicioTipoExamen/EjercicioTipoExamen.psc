Algoritmo sin_titulo
	seguir = "si"
	result = 0
	Mientras seguir = "si" Hacer
		Escribir "Ingresar un número: "
		Leer num
		Escribir "Ingresar otro número: "
		Leer num2
		Escribir "Elegir: 1-suma 2-resta"
		Leer opc
		Si opc = 1 Entonces
			result = num+num2
		SiNo
			Si opc = 2 Entonces
				result = num-num2
			FinSi
		Fin Si
		Escribir "Resultado: ",result
		Escribir "Quiere seguir? [si/no]"
		Leer seguir
	Fin Mientras
	
FinAlgoritmo
