#TERMINADO

"""Alertas meteorológicas: acá se deberá controlar ciertos valores y cantidades para dar
alertas meteorológicas.

Se debe ingresar una cantidad de temperaturas promedios durante cierta
cantidad de días para prever que pasara en los días posteriores. Nos pasaron los
siguientes datos y requerimientos sobre el módulo:

 Se sabe que cuando una temperatura supera los 30 es alta, cuando está por
debajo de 11 es baja y en el resto es templada.
 El usuario deberá ingresar temperaturas hasta haber terminado sin ingresar
previamente la cantidad. Pero saber que el máximo de días, que puede
registrar, es de 11.
 Si se registra que hubo 7 días o más con temperaturas altas, quiere decir que
vendrá una ola de calor.
 Si se registras que hubo 5 días o más con temperaturas bajas, quiere decir que
vendrá una ola polar.
 En caso que no ocurra ninguna de las dos tendremos un buen tiempo."""

tempAltas = 0
tempBajas = 0
tempTempladas = 0

temperaturas = [0,0,0,0,0,0,0,0,0,0,0]

def defTemp(temperatura):
    if temperatura > 30:
        global tempAltas
        tempAltas+= 1
    elif temperatura < 11:
        global tempBajas
        tempBajas+=1
    else:
        global tempTempladas
        tempTempladas+=1

def defOla():
    if tempAltas >= 7:
        return "Vendra una ola de calor."
    elif tempBajas >= 5:
        return "Vendra una ola polar."
    else:
        return "Tendremos un buen tiempo."

for i in range(11):
    print("Ingrese la temperatura del día ",i+1,":",end="")
    temperaturas[i] = int(input())
    defTemp(temperaturas[i])

print("\n",defOla(),"\n")
print("Temperaturas altas: ",tempAltas,"\nTemperaturas bajas: ",tempBajas,"\nTemperaturas Templadas: ",tempTempladas)