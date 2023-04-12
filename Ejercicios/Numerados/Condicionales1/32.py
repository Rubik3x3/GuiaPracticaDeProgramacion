"""Ingresar 5 números. Informar cuantos números se encuentran 
entre 600 y 800 y cuantos entre 850 y 1500. """

numeros=[0,0,0,0,0]
entre_600_800=0
entre_850_1500=0

for i in range(5):
    print("Ingrese el número ",i)
    numeros[i] = int(input())

    if numeros[i] >= 600 and numeros[i] <= 800:
        entre_600_800+=1
    elif numeros[i] >= 850 and numeros[i] <= 1500:
        entre_850_1500+=1

print("Números: ",numeros,"\n\nNúmeros entre 600 y 800: ",entre_600_800,"\nNúmeros entre 850 y 1500: ",entre_850_1500)

