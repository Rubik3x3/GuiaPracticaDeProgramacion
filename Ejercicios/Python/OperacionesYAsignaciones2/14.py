"""Dado el nombre de un empleado, el sueldo básico y la antigüedad, mostrar 
el sueldo completo y el nombre del empleado. Saber que al sueldo básico se le 
adiciona el plus por antigüedad. La antigüedad es un porcentaje del sueldo."""

nombre=str(input("Nombre del empleado:\n"))
sueldoBasico=int(input("Ingrese el sueldo básico:\n"))
antiguedad=int(input("Antigüedad:\n"))

sueldoCompleto = sueldoBasico + ((sueldoBasico*antiguedad)/100)

print("\nNombre: ",nombre,"\n","Sueldo Completo: $",sueldoCompleto)