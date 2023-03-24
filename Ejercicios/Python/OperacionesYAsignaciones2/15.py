"""Para el pago de sueldos ingresan $45210 mensuales. Se pide ingresar 6 sueldos y
#mostrar que porcentaje del ingreso se necesita para pagar el total de esos sueldos."""

pagoIngresado = 45210
sueldos = [0,0,0,0,0,0]
totalSueldos = 0

for i in range(6):
    print("Ingrese el sueldo número ",i+1)
    sueldos[i] = int(input())
    totalSueldos+=sueldos[i]

porcentajeIngreso = totalSueldos*100/pagoIngresado

print("Total de sueldos: $",totalSueldos)
#print(sueldos)
print("Se necesita un ",porcentajeIngreso,"porciento del ingreso.")