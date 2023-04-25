"""
El Gamer ingresa los scores obtenidos en una partida (X rondas) y el programa deberá
decirme, con los lotes formados entre 2 números impares:

a. La productoria de dichos scores, la sumatoria por cada lote.

b. Cuantos valores positivos por cada lote y cuantos lotes hay en total
"""

score = 0

productoria = 0
sumatoria = 0

valPositivos = 0
cuenta = 0

#Mientras el score sea par:
while score % 2 == 0:
    score = int(input("Ingrese un score: "))

#Mientras sea impar:
while score % 2 != 0:
    score = int(input("Ingrese un score para el lote: "))
    if cuenta == 0:
        productoria = score
        sumatoria = score
    else:
        productoria *= score
        sumatoria += score

    if score >= 0:
        valPositivos += 1

    cuenta += 1
    
#Mostrar datos
print("Productoria: ",productoria)
print("Sumatoria: ",sumatoria)
print("Valores positivos: ",valPositivos)
print("Lotes en total: ",cuenta)



