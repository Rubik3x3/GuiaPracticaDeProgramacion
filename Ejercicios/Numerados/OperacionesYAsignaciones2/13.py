"""Dado 4 sueldos de empleados mostrar el dinero necesario para pagar todos ellos."""

sueldos=[0,0,0,0]
total=0
for i in range(4):
    print("Ingrese el sueldo Nº",i+1)
    sueldos[i]=int(input())
    total+=sueldos[i]
print("Total de dinero para pagar los 4 sueldos: $",total)