"""
Evaluación Integradora: Programación
Fecha: miércoles 26 de abril, 2023
Puntaje:
"""

"""
NOTA: ser concisos al redactar las respuestas y al desarrollar el
programa. Entregar la evaluación en tinta.
"""

#1 - TEORIA

# a. Secuencia, condicional
# b.
def c():
	result = int(0)
	seguir = "si"

	while seguir == "si":
		num = int(input("Ingresar un numero: "))
		otroNum = int(input("Ingresar otro número: "))
		opc = int(input("Elegir: 1-suma 2-resta"))
		if opc == 1:
			result = num+otroNum
		else:
			if opc == 2:
				result = num-otroNum	
		print("Resultado: ",result)
		seguir = str(input("Quiere seguir? [si/no]"))

# c. EjercicioTipoExamen.psc

"""

Instrución: La instrucción es la órden o directiva a la computadora de que haga algo.
Diseño: Son los pasos de planificacion antes de comenzar a escribir el código.
Algoritmo: Un algoritmo es un conjunto de instrucciones que indican a la computadora como ejecutar una tarea. 

"""

#2 - PRÁCTICA

"""
Desarrollar un programa que cumpla con el siguiente enunciado:

Se pone en órbita un satélite que mide la temperatura terrestre para hacer evaluaciones
del calentamiento global. El usuario, que se encarga del satélite podrá elegir dos opciones
hasta que termine su turno, es decir, el avisará cuando dejará de seguir en el control.

a. Control de satélite: Se ingresa la velocidad del mismo. Si está fuera del rango normal
se realiza una corrección orbital.

b. Lecturas de temperatura: se ingresa la temperatura y región medida.
Un satélite de este tipo, para permanecer en órbita necesita estar a una velocidad, como
rango normal, entre 15mil Km/h y 16mil Km/h.

La corrección orbital consiste en calcular el 1.67% de la velocidad y sumársela si está por
debajo del rango o restársela si esta por arriba. Esto se hará tantas veces como sea necesario,
hasta ubicarse en el rango normal.

Al finalizar, se deberá informar cuantas fueron las temperaturas registradas superiores a
30.
"""


seguir = str("si")
CO = float(1.67)

velocidad = int(0)
temperatura = int(0)

while seguir == "si":
	opc = int(input("Opciones: [1] Control de satélite [2] Lecturas de temperatura"))
	if opc == 1:
		velocidad = int(input("Ingrese la velocidad del satélite: "))

