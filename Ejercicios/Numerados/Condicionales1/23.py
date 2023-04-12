"""Realizar un programa que controle la entrada de personas a 
un establecimiento. Habría que ingresar la edad de la persona 
y el sistema le informará si podrá ingresar o no. 
Para ello la persona debe ser mayor de edad."""

edad=int(input("Ingrese la edad de la persona:\n"))
if edad >= 18:
    print("La persona puede ingresar.\nEs mayor de edad.")
else:
    print("La persona no puede ingresar.\nEs menor de edad.")