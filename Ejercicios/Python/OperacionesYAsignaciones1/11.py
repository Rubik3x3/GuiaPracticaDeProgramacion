"""Realizar un programa que permita realizar las siguientes operaciones matemática:
potencia y resto. Mostrar los resultados por pantalla."""

print("¿Qué operación quieres realizar?\n[1] Resto\n[2] Potencia")
operacion=int(input())

print("Operación Nº",operacion)

numero1=int(input("Ingrese el número 1:\n"))
numero2=int(input("Ingrese el número 2:\n"))

if operacion == 2:
    print("El ",numero1," elevado a ",numero2,"=",numero1**numero2)
elif operacion == 1:
    print("El resto de ",numero1,"/",numero2,"=",numero1%numero2)
else:
    print("Ingrese un número de operación válido.")