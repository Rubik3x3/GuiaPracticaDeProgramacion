"""Se ingresan el largo, ancho y el valor del metro cuadrado de un terreno. Mostrar el
#valor total del terreno."""

largoDelTerreno=int(input("Ingrese el largo del terreno:\n"))
anchoDelTerreno=int(input("Ingrese el ancho del terreno:\n"))
valorPorM2=int(input("Ingrese el valor por metro cuadrado del terreno:\n"))

areaDelTerreno=largoDelTerreno*anchoDelTerreno
valorDelTerreno=areaDelTerreno*valorPorM2

print("\nEl área total del terreno es de: ",areaDelTerreno," metros cuadrados.\nEl valor del terreno es de: $",valorDelTerreno)