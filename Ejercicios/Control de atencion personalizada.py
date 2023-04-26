"""
Control de atención personalizada: este módulo se usará en un dispositivo para que el
empleado pueda ir expresando su satisfacción de acuerdo a la atención recibida. Esto

será para la parte administrativa de la organización. Ya sea para la entrega de recibos,
chequeos y firmas de papeles, entrega de certificados de descubrimientos, etc… Toda
la parte administrativa se maneja entre 4 oficinas, la 309, la 318, mesa de entrada y la
oficina de empleados.

El empleado comienza dirigiéndose a la oficina de empleados donde explica su
problema y de ahí lo derivan a la oficina correspondiente. Allí comienza su odisea
burocrática. En cuanto a la funcionalidad:

-El usuario ingresa la oficina a la cual tiene que ir.

-El usuario comienza con 100 de paciencia.

-Puede suceder que se solucione su problema o que no se soluciones y lo
manden a otra oficina.

-El uso de la aplicación termina cuando su problema se solucione.

-Si tiene le dicen que debe ir a otra oficina, a la paciencia se le descuenta 30.

-En la “mesa de entrada” no se resuelva ningún problema, ya que como se vio
en otro modulo solo se encarga de la entrada y salida de empleados.

-Si la paciencia llega a 0, el empleado tendrá “un día de furia”. Y se le deberá
informar al cuerpo de seguridad que “controle la situación”. Allí también se
acaba el funcionamiento del programa.
"""

paciencia = 100
problemaSolucionado = False
problema = ""
def solucionarProblema(oficina):
	global paciencia
	print("Te encuentras en la oficina ",oficina)
	ans = str(input("Solucionaron tu problema? [si/no]"))
	if ans == "si":
		print("Problema solucionado.")
		exit()
	else:
		paciencia -= 30
		if paciencia <= 0:
			print("El emplezado tiene un día de furia")
			print("El cuerpo de seguridad debe controlar la situacion.")
			exit()
print("Te encuentras en la mesa de entrada.")

problema = str(input("Ingrese el problema que tiene: "))

while problemaSolucionado == False:
	print("A qué oficina lo dirigen? \n"+oficinas)
	off = int(input())

	if off == 1:
		solucionarProblema("309")
	elif off == 2:
		solucionarProblema("318")
	elif off == 3:
		solucionarProblema("de empleados")
	else:
		print("No existe esa oficina")
