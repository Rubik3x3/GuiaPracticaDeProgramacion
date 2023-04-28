# 3ra Evaluación Integradora: Programacion - Franco Talarico 3º1 - 26/04/2023 - Nota: 5/5

"""
Programacion:

Desarrollar un programa que cumpla con el siguiente enunciado:

Una empresa de juegos necesita que desarrollemos un modulo para un juego de mundo abierto. En el mismo se necesita representar la siguiente funcionalidad:
Al comenzar, el jugador, puede elegir la clase de presonaje con la que quiere juegar. Dichas clases son: mago, arquero o guerrero. Sea cual sea la clase
va a comenzar con una cantidad de oro inicial, dada por el usuario, y un atributo arma.
Dentro de las acciones que hay que programar, el jugador podrá elegir alguna de las siguientes:

a) Viajar por el mundo: donde el jugador irá ingresando el nombre de las ciudades que irá visitando hasta que elija parar con su viaje. 
Por cada ciudad aumenta la cantidad en oro en 25 monedas.

b) Comprar arma: donde se ingresa el arma que se comprara y su precio. Los guerreros siempre obtienen un descuento del 10%. 
SABER: hay que corroborar que cuente con dinero disponible.

Al finalizar se deberá informar al jugador:
arma, oro y cantidad de ciudades visitadas.

NOTA: no es necesario que el usuario elija otra acción luego de terminar una.

"""

ciudades = 0
clase = str(input("Ingrese la clase del personaje: [mago/arquero/guerrero]: "))
oro = int(input("Ingrese la cantidad de oro: "))

arma = str(input("Ingrese el arma: "))

opc = int(input("Acciones:\n[1] Aventurarse\n[2] Comprar arma\nOpción: "))

if opc == 1:
    seguir = "si"
    while seguir == "si":
        c = str(input("Ingrese el nombre de la ciudad: "))
        oro += 25
        ciudades += 1

        print("Visitaste ", c, " y conseguiste 25 de oro.")

        seguir = str(input("Quiere visitar más ciudades? [si/no]: "))
elif opc == 2:
    a = str(input("Arma a comprar: "))
    precio = int(input("Precio del arma: "))

    if oro >= precio:
        if clase == "guerrero":
            precio -= (precio*10)/100
            arma = a
            oro -= precio
        else:
            arma = a
            oro -= precio
        print("Compraste el arma ", a,)

    else:
        print("No tienes suficiente dinero.")

print("Arma: ", arma)
print("Oro: ", oro)
print("Ciudades visitadas: ", ciudades)
