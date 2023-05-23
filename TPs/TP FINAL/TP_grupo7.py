import os
import time

# Información Base
dineroDisponibleInicial = int(875000)
sueldoBasico = int(8875)

# USUARIOS, CONTRASEÑAS, AREA EN NÚMERO Y AREA
userSecAdministrativoOficinas = [
    "user1", "pass1", 1, "Sector Administrativo Oficinas"]

userSecAdministrativoRecepcion = [
    "user2", "pass2", 2, "Sector Administrativo Recepción"]

userDesarrolladores = ["user3", "pass3", 3, "Desarrolladores"]

userGerentes = ["user4", "pass4", 4, "Gerentes"]

userRRHH = ["user5", "pass5", 5, "Recursos Humanos"]

userControlDeRecursos = ["user6", "pass6", 6, "Control de Recursos"]

usuariosTOTALES = [userSecAdministrativoOficinas, userSecAdministrativoRecepcion,
                   userDesarrolladores, userGerentes, userRRHH, userControlDeRecursos]

# Limpia la pantalla


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Login de usuario y contraseña


def login():

    clear()
    logueado = False
    usuarioFinal = []
    acumuladorUsuarios = 0

    userLogueado = str(input("Ingresar el Usuario: "))

    for usuario in usuariosTOTALES:
        if usuario[0] == userLogueado:
            clear()

            print("Usuario: ", userLogueado, sep="")

            passLogueada = str(input("Ingresar la Contraseña: "))

            if usuario[1] == passLogueada:
                logueado = True
                usuarioFinal = usuario

        acumuladorUsuarios += 1

    if logueado:
        clear()
        print(
            f'Logueado correctamente.\n\nUsuario: {usuarioFinal[0]}\nÁrea: {usuarioFinal[3]}')

        return usuarioFinal[0], usuarioFinal[1], usuarioFinal[2], usuarioFinal[3]
    else:
        clear()
        print("No se pudo loguear.")
        time.sleep(1)
        login()


def sector_administrativo_oficinas(login):
    continuar = 1
    while continuar == 1:
        clear()
        print(
            "\nOpciones:\n\n[1] Sueldos\n[2] Gastos varios\n[3] Proyectos vendidos\n[4] Cerrar sesión")

        opc = int(input("\nOpción seleccionada: "))

        if opc == 1:
            print("Sueldos.")
            continuarEmpleados = 1
            while continuarEmpleados == 1:
                clear()
                nombreEmpleado = str(input("Ingrese el nombre del empleado: "))
                dniEmpleado = int(input("Ingrese el DNI del empleado: "))
                puestoEmpleado = str(input(
                    "Ingrese el puesto del empleado Desarrollador/Gerente/Administrativo/Trainer/CEO:"))
                plusEmpleado = int(input("Ingrese el plus del empleado: $"))

                if puestoEmpleado == "Desarrollador":
                    sueldoFinal = ((sueldoBasico*240)/100)+plusEmpleado
                elif puestoEmpleado == "Gerente":
                    sueldoFinal = sueldoBasico + \
                        ((sueldoBasico*350)/100)+plusEmpleado
                elif puestoEmpleado == "Administrativo":
                    sueldoFinal = sueldoBasico+plusEmpleado
                elif puestoEmpleado == "Trainer":
                    sueldoFinal = ((sueldoBasico*70)/100)+plusEmpleado
                elif puestoEmpleado == "CEO":
                    sueldoFinal = (sueldoBasico*9.8)+plusEmpleado

                clear()

                print("Sueldo: $", sueldoFinal)
                print("Presupuesto: $", dineroDisponibleInicial)

                if dineroDisponibleInicial >= sueldoFinal and dniEmpleado % 2 != 0:
                    print("Se puede pagar a dicho empleado.")
                else:
                    print("No se le puede pagar al empleado.")

                continuarEmpleados = int(
                    input("\n¿Quiere continuar cargando empleados? [1] Sí - [2] No : "))

        elif opc == 2:
            print("Gastos vendidos.")
            tipoArticulo = str(input("Ingrese el tipo de artículo: "))
            montoArticulo = str(input("Ingrese el monto del artículo: "))

        elif opc == 3:
            print("Proyectos vendidos.")
            nombreProyecto = str(input("Ingrese el nombre del proyecto: "))
            montoProyecto = str(input("Ingrese el monto del proyecto: "))

        elif opc == 4:
            if os.name == "nt":
                os.system("python TP_grupo7.py")
            else:
                os.system("python3 TP_grupo7.py")


def sector_administrativo_recepcion():
    print("Recepcion")


def gerentes():
    pass


def desarrolladores():
    pass


def recursos_humanos():
    pass


def control_de_recursos():
    pass


def areas(area, login):
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

areas(login[2], login)
