"""Dado un número, mostrar si pertenece al grupo A o al grupo B. 
Los del grupo A se encuentran entre 30 y 60. 
Mientras que los del grupo B entre 70 y 80."""

numero=float(input("Ingrese un número:\n"))

if numero >= 30 and numero <= 60:
    print("El número está en el grupo A.")
elif numero >= 70 and numero <= 80:
    print("El número está en el grupo B.")
else:
    print("El número no está en ningún grupo.")