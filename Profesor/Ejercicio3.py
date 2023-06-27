"""
Escribir un programa que pida al usuario 10 numeros
los agregue a una lista y que luego muestre por pantalla
el menor el mayor y el promedio.
"""

numeros = []
mayor = int(0)
menor = int(0)
acumulador = int(0)
promedio = int(0)

cont = int(0)

for i in range(10):
	numero = int(input(f'Ingrese el número {i+1}: '))
	numeros.append(numero)

	acumulador += numero

for numero in numeros:
	if cont == 0:
		menor = numero
		mayor = numero
	else:
		if menor > numero:
			menor = numero
		if mayor < numero:
			mayor = numero

promedio = acumulador/10

print(f'Número mayor: {mayor}')
print(f'Número menor: {menor}')
print(f'Promedio: {promedio}')