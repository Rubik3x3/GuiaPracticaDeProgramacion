"""Dado 4 sueldos de empleados mostrar el dinero necesario para 
pagar todos ellos.Y también, mostrar el sueldo promedio 
NOTA: realizar este ejercicio con un máximo de 3 variables"""

sueldo = 0
totalSueldos = 0
for i in range(4):
    print("Ingrese el sueldo del empleado ",i+1)
    sueldo=int(input())
    totalSueldos += sueldo
    sueldo = 0

print("\nEl promedio de los sueldos es de $",totalSueldos/4)