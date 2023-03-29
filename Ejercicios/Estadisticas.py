"""Estadísticas: este módulo se usará para el proyecto que automatiza la creación de
estadísticas según los valores de meteorológicos que se ingresan.

Se necesita ingresar cierta cantidad de temperaturas con sus respectivos
horarios registradas en el mismo día. Como resultado deberemos ver cuál fue la
temperatura más alta con su horario, cual la temperatura mínima con su horario y cual
la temperatura promedio."""

horas = ["00:00hs","01:00hs","02:00hs","03:00hs","04:00hs","05:00hs","06:00hs","07:00hs","08:00hs","09:00hs","10:00hs","11:00hs","12:00hs","13:00hs","14:00hs","15:00hs","16:00hs","17:00hs","18:00hs","19:00hs","20:00hs","21:00hs","22:00hs","23:00hs",]

iTemperaturas=str(input("Ingrese el promedio de temperatura en cada hora del día [Ej: 1,2,3...]:\n"))

temperaturas=iTemperaturas.split(",",24)

tempTotal = 0
tempMax = -100
tempMin = 100

tempPromedio = 0

cuenta = 0

for i in temperaturas:
	print("Promedio de temperatura a las ",horas[cuenta],": ",i)

	tempTotal += int(i)

	if tempMax < int(i):
		tempMax = int(i)
	elif tempMin > int(i):
		tempMin = int(i)

	cuenta += 1

print("\nLa temperatura minima en el día fue: ",tempMin)
print("La temperatura máxima en el día fue: ",tempMax)

tempPromedio = tempTotal/cuenta

print("La temperatura promedio del día fue: ",tempPromedio)