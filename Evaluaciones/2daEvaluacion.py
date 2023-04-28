# 2da Evaluación de Taller - Franco Talarico - 3º1 11/04/2023 - Nota: 4/5

"""
Sistemas de gestión de tormentas
Se debe registrar la duración total y la intensidad (de 1 a 10) de una tormenta en 1 día.
Luego de eso se debe informar:

1) El nivel de la tormenta: Medio o Alto. Medio será cuando la duración esté entre 15 y 40 minutos y con intensidad entre 5 y 7. 
Nivel alto con duración entre 40 y 60 minutos y con intensidad entre 6 y 10.

2) Si se debe emitir una alerta. Esto ocurre cuando la intensidad es superior a 8.

3) Porecentaje del día libre de tormenta.
"""

porcentajeTormenta = 0
porcentajeLibre = 0

duracion = int(input("Ingrese la duración de la tormenta en minutos: "))
intensidad = int(input("ingrese la intensidad de la tormenta [1-10]: "))

if duracion >= 15 and duracion <= 40 and intensidad >= 5 and intensidad <= 7:
    print("Nivel de la tormenta: MEDIO")
elif duracion > 40 and duracion <= 60 and intensidad >= 6 and intensidad <= 10:
    print("Nivel de la tormenta: ALTO")

porcentajeTormenta = ((100*duracion)/1440)
porcentajeLibre = 100 - porcentajeTormenta

print("Porcentaje del día libre de tormenta: ", porcentajeLibre)

if intensidad > 8:
    print("¡ALERTA! Intensidad mayor a 8.")
