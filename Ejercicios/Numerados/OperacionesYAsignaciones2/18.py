"""Dado un terreno cuadrado se ingresa el largo, en metros, de uno de los lados de dicho
terreno. Se debe mostrar el área total del terreno y su valor por metro cuadrado,
sabiendo que el valor total es de $2567."""

largoDelTerreno=int(input("Ingrese el largo del terreno:\n"))
valorPorM2=2567
areaDelTerreno=largoDelTerreno*largoDelTerreno

valorDelTerreno=valorPorM2*areaDelTerreno

print("\nEl área total del terreno es de: ",areaDelTerreno," metros cuadrados.\nEl valor del terreno es de: $",valorDelTerreno)