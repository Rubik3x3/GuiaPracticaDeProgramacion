"""Test de alcoholemia. Dado un puntaje de alcohol en sangre decir 
si el ingresante está o no alcoholizad. Eso dependerá si ese 
puntaje es mayor a 0.5"""

alcoholEnSangre=float(input("Ingrese el alcohol en sangre:\n"))

if alcoholEnSangre > 0.5:
    print("El ingresante está alcoholizado.")
else:
    print("El ingresante no está alcoholizado.")