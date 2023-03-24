"""Dado el radio de un terreno circular y los lados (largo y ancho) de un terreno
rectangular. Calcular el valor total de ambos terrenos sabiendo que el valor de los
metros cuadrado es ingresado por pantalla. NOTA: el valor de pi = 3,14"""

PI=3.14

radioDelTerreno=int(input("Ingrese el radio del terreno 1:\n"))
largoDelTerreno2=int(input("Ingrese el largo del terreno 2:\n"))
anchoDelTerreno2=int(input("Ingrese el ancho del terreno 2:\n"))
valorPorM2=int(input("Ingrese el valor por metro cuadrado:\n"))

terreno1=PI*radioDelTerreno*radioDelTerreno
terreno2=largoDelTerreno2*anchoDelTerreno2

valorTotalM2=(terreno1+terreno2)*valorPorM2

print("\nTerreno 1:",terreno1," metros cuadrados.","\nTerreno 2:",terreno2," metros cuadrados.","\n\nTerreno Total:",terreno1+terreno2," metros cuadrados.\nEl valor total de ambos terrenos es de: $",valorTotalM2)