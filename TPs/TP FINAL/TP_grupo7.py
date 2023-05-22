import os,time

#Información Base
dineroDisponibleInicial = int(875000)
sueldoBasico = int(8875)

# USUARIOS, CONTRASEÑAS, AREA EN NÚMERO Y AREA
userSecAdministrativoOficinas = ["user1","pass1",1,"Sector Administrativo Oficinas"]

userSecAdministrativoRecepcion = ["user2","pass2",2,"Sector Administrativo Recepción"]

userDesarrolladores = ["user3","pass3",3,"Desarrolladores"]

userGerentes = ["user4","pass4",4,"Gerentes"]

userRRHH = ["user5","pass5",5,"Recursos Humanos"]

userControlDeRecursos = ["user6","pass6",6,"Control de Recursos"]

usuariosTOTALES = [userSecAdministrativoOficinas,userSecAdministrativoRecepcion,userDesarrolladores,userGerentes,userRRHH,userControlDeRecursos]

#Limpia la pantalla
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

#Login de usuario y contraseña
def login():

	clear()
	logueado = False
	usuarioFinal = []
	acumuladorUsuarios = 0

	userLogueado = str(input("Ingresar el Usuario: "))

	for usuario in usuariosTOTALES:
		if usuario[0] == userLogueado:
			clear()

			print("Usuario: ",userLogueado,sep="")

			passLogueada = str(input("Ingresar la Contraseña: "))

			if usuario[1] == passLogueada:
				logueado = True
				usuarioFinal = usuario

		acumuladorUsuarios += 1

	if logueado:
		clear()
		print(f'Logueado correctamente.\n\nUsuario: {usuarioFinal[0]}\nÁrea: {usuarioFinal[3]}')

		return usuarioFinal[0],usuarioFinal[1],usuarioFinal[2],usuarioFinal[3]
	else:
		clear()
		print("No se pudo loguear.")
		time.sleep(1)
		login()

def sector_administrativo_oficinas(login):
	continuar = 1
	while continuar == 1:
		print("\nOpciones:\n\n[1] Sueldos\n[2] Gastos varios\n[3] Proyectos vendidos\n[4] Cerrar sesión")

		opc = int(input("\nOpción seleccionada: "))

		if opc == 1:
			print("Sueldos.")

			while True:
				nombreEmpleado = str(input("Ingrese el nombre del empleado: "))
				dniEmpleado = int(input("Ingrese el DNI del empleado: "))
				puestoEmpleado = str(input("Ingrese el puedo del empleado: "))
				plusEmpleado = int(Input("Ingrese el plus del empleado"))


		elif opc == 2:
			print("Gastos vendidos.")
			tipoArticulo = str(input("Ingrese el tipo de artículo: "))
			montoArticulo = str(input("Ingrese el monto del artículo: "))

		elif opc == 3:
			print("Proyectos vendidos.")
			nombreProyecto = str(input("Ingrese el nombre del proyecto: "))
			montoProyecto = str(input("Ingrese el monto del proyecto: "))

		elif opc == 4:
			os.system("python TP_grupo7.py")	

def sector_administrativo_recepcion():
	pass

def gerentes():
	pass

def desarrolladores():
	pass

def recursos_humanos():
	pass

def control_de_recursos():
	pass

def areas(area,login):
	if area == 1:
		sector_administrativo_oficinas(login)
	elif area == 2:
		sector_administrativo_recepcion()
	elif area == 3:
		gerentes()
	elif area == 4:
		desarrolladores()
	elif area == 5:
		recursos_humanos()
	elif area == 6:
		control_de_recursos()

login = login()

areas(login[2],login)

