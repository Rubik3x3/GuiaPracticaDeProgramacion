"""Realizar un programa que permita realizar las 4 operaciones matemáticas: suma, resta,
división y multiplicación. Mostrar los resultados por pantalla."""

print("¿Qué operación quieres realizar?\n[1] Suma\n[2] Resta\n[3] Multiplicación\n[4] División")
operacion=int(input())

print("Operación Nº",operacion)

numero1=int(input("Ingrese el número 1:\n"))
numero2=int(input("Ingrese el número 2:\n"))

if operacion == 1:
    print("La suma de ",numero1,"+",numero2,"=",numero1+numero2)
elif operacion == 2:
    print("La resta de ",numero1,"-",numero2,"=",numero1-numero2)
elif operacion == 3:
    print("La multiplicación de ",numero1,"x",numero2,"=",numero1*numero2)
elif operacion == 4:
    print("La división de ",numero1,"/",numero2,"=",numero1/numero2)
else:
    print("Ingrese un número de operación válido.")