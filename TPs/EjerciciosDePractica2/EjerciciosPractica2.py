#Franco Talarico 3°1

"""
Debido a las restricciones sanitarias en una semana solo pueden viajar 3 personas en
esta agencia.

La agencia debe ingresar, ciertos datos, de cada cliente para poder obtener las
estadísticas. Dichos datos son: nombre, DNI, si es o no internacional el viaje y el monto.

Para fomentar el turismo se aplican ciertos descuentos bajo ciertos criterios:

 Si la persona tiene el DNI menor a 28 millones: descuento del 27.2%
 Pero si la persona tiene el DNI menor a 28millones y además viaja al exterior el
descuento total es de 22.8%.
 Si la persona tiene el DNI mayor o igual a 28 millones: descuento del 10%

Al terminar de ingresar los 3 clientes se le deberá informar a la agencia cuantos vuelos
son internacionales y cuanto es el ingreso total obtenido por los 3 clientes.
"""

vuelosInter = 0
ingresoTotal = 0.0

def aplicarDescuento(precio,descuento):
	precioConDescuento = precio-(precio*descuento)/100
	return precioConDescuento

def viaje(dni,inter,monto):
	global vuelosInter,ingresoTotal
	if dni < 28000000:
		if inter != "si":
			desc = float(27.2)
			vuelosInter+=1
		else:
			desc = float(22.8)
	else:
		desc = float(10)

	monto = aplicarDescuento(monto,desc)
	ingresoTotal+=monto

	print("El monto final del viaje es de: $",monto)

for i in range(3):
	iNombre=str(input("Ingrese su nombre: "))
	iDni=int(input("Ingrese su DNI: "))
	iInter=str(input("¿Su viaje es internacional? [si/no]: "))
	iMonto=float(input("Ingrese el monto: "))
	viaje(iDni,iInter,iMonto)


print("Hay ",vuelosInter," vuelos internaciones.\nEl ingreso total de los 3 clientes es de: $",ingresoTotal,sep="")
