"""Dado un numero ingresado, calcular el 40% del mismo. 
Luego informar si dicho valor se encuentra entre 100 y 250 o entre 300 y 500."""

numero=int(input("Ingrese un número:\n"))
porciento=numero*0.4
if porciento >= 100 and porciento <= 250:
    print("El número se encuentra entre 100 y 250.")
elif porciento >= 300 and porciento <= 500:
    print("El número se encuentra entre 300 y 500")
else:
    print("El número no se encuentra entre 100-250 ni 300-500.")