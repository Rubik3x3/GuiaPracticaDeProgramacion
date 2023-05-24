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

ingresosTotales = int(0)
gastosTotales = int(0)
sueldoMasBajo = int(0)
sueldoMasAlto = int(0)

horarioMayorCantEmpleadosOrganizacion = ""

proyectoMasPrioridad = int(0)



login = []

# Limpia la pantalla


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Login de usuario y contraseña


def login():
    global login
    login = []

    logueado = False
    while logueado == False:
        clear()
        logueado = False
        usuarioFinal = []
        acumuladorUsuarios = 0
        print("[ Proyecto Gestión Interna - Unicron S.A ] LOGIN\n")
        userLogueado = str(input("Ingresar el Usuario: "))

        for usuario in usuariosTOTALES:
            if usuario[0] == userLogueado:
                clear()
                print("[ Proyecto Gestión Interna - Unicron S.A ] LOGIN\n")
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

            login = usuarioFinal[0], usuarioFinal[1], usuarioFinal[2], usuarioFinal[3]
            areas(login[2])

        else:
            clear()
            print("No se pudo loguear.")
            time.sleep(1)

# Termina el programa y lo vuelve a iniciar


def cerrar_sesion():
    global login
    login = []
    if os.name == "nt":
        os.system("python TP_grupo7.py")
    else:
        os.system("python3 TP_grupo7.py")


def calcular_puntos(semanas, paga, modulos, tareas):
    puntos = float(0)
    puntos = (0.7*semanas)+(0.00005*paga)+modulos+(5*tareas)

    if puntos > 100:
        puntos = float(100)

    puntos = round(puntos)
    return puntos

def cargo_a_ocupar(pProgramacion,pTrabajoEquipo,pOrden,pCreatividad,telefono,ocupacion):
    if pProgramacion>=6 and pTrabajoEquipo>=7 and pOrden>=4 and pCreatividad>=7 and telefono % 2 == 1 and ocupacion==1:
        cargo=str("Desarrollador")

    elif pProgramacion>=0 and pTrabajoEquipo>=6 and pOrden>=7 and pCreatividad>=2 and telefono % 2 == 1 and ocupacion==2:
        cargo=str("Administrador")

    elif pProgramacion>=2 and pTrabajoEquipo>=6 and pOrden>=8 and pCreatividad>=3 and telefono % 2 == 1 and ocupacion==3:
        cargo=str("Controlador de Recursos")

    elif pProgramacion>=0 and pTrabajoEquipo>=6 and pOrden>=7 and pCreatividad>=2 and telefono % 2 == 1 and ocupacion==4:
        cargo=str("Recursos Humanos")
    else:
        cargo = str("")

    return cargo

def sector_administrativo_oficinas():
    global login, dineroDisponibleInicial, sueldoBasico

    continuar = 1
    while continuar == 1 and login != []:
        clear()
        print(
            "\n[ MENÚ SECTOR ADMINISTRATIVO (oficinas)]:\n\n[1] Sueldos\n[2] Gastos varios\n[3] Proyectos vendidos\n[4] Cerrar sesión")

        opc = int(input("\n\n->   "))

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
                    input("\n¿Quiere continuar cargando empleados?\n\n[1] Sí\n[2] No\n\n->  "))

        elif opc == 2:
            continuarGastos = 1
            totalGasto = 0
            while continuarGastos == 1:
                clear()
                print("Gastos vendidos.")
                tipoArticulo = str(input("Ingrese el tipo de artículo: "))
                montoArticulo = int(input("Ingrese el monto del artículo: "))

                totalGasto += montoArticulo

                print(
                    f'Dinero antes de la compra: $ {dineroDisponibleInicial}\nDinero a gastar: ${montoArticulo}\nDinero final: ${dineroDisponibleInicial-montoArticulo}\n\nGasto total: {totalGasto}')
                dineroDisponibleInicial -= montoArticulo
                continuarGastos = int(
                    input("\n¿Quiere continuar ingresando artículos?\n\n[1] Sí\n[2] No\n\n->  "))

        elif opc == 3:
            continuarProyectos = 1
            while continuarProyectos == 1:
                print("Proyectos vendidos.")
                nombreProyecto = str(input("Ingrese el nombre del proyecto: "))
                montoProyecto = str(input("Ingrese el monto del proyecto: "))

                print(
                    f'Dinero inicial: ${dineroDisponibleInicial}\nDinero final: ${dineroDisponibleInicial+montoProyecto}')

                dineroDisponibleInicial += montoProyecto

                continuarProyectos = int(
                    input("\n¿Quiere continuar ingresando proyectos?\n\n[1] Sí\n[2] No\n\n->  "))

        elif opc == 4:
            cerrar_sesion()


def sector_administrativo_recepcion():
    continuar = 1

    while continuar == 1 and login != []:
        clear()
        print(
            "\n[ MENÚ SECTOR ADMINISTRATIVO (recepción)]:\n\n[1] Calcular empleados\n[2] Cerrar sesión")

        opc = int(input("\n->  "))

        if opc == 1:
            continuarCalcEmpleados = 1
            while continuarCalcEmpleados == 1:
                totalEmpleados = 0
                empleadosEnLaOrganizacion = 0

                empleadosPorHora = [0, 0, 0, 0, 0,
                                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                salen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                entran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                horas = ["6:00hs", "7:00hs", "8:00hs", "9:00hs", "10:00hs", "11:00hs", "12:00hs",
                         "13:00hs", "14:00hs", "15:00hs", "16:00hs", "17:00hs", "18:00hs", "19:00hs", "20:00hs"]

                for i in range(15):
                    clear()
                    print(
                        "\nIngrese la cantidad de empleados que entran en la hora: ", horas[i], "\n")
                    iEntran = int(input())
                    print(
                        "\nIngrese la cantidad de empleados que salen en la hora: ", horas[i], "\n")
                    iSalen = int(input())

                    salen[i] = iSalen
                    entran[i] = iEntran

                    empleadosEnLaOrganizacion += (entran[i]-salen[i])
                    empleadosPorHora[i] = empleadosEnLaOrganizacion

                    totalEmpleados += entran[i]

                    print("\nEmpleados en la organizacion: ",
                          empleadosEnLaOrganizacion)
                    print(
                        "En la hora ", horas[i], ":\nEntran: ", entran[i], "\nSalen: ", salen[i])

                clear()

                for i in range(15):
                    print("\nA las ", horas[i], " entran ",
                          entran[i], " empleados y salen ", salen[i])
                    print("Empleados en la organizacion: ",
                          empleadosPorHora[i])
                print("\n>> Empleados totales de la organizacion: ",
                      totalEmpleados)

                continuarCalcEmpleados = int(
                    input("\n¿Quiere continuar calculando empleados? \n\n[1] Sí\n[2] No\n\n->  "))
        elif opc == 2:
            cerrar_sesion()


def desarrolladores():
    continuar = 1

    while continuar == 1 and login != []:
        clear()
        print(
            "\n[ MENÚ DESARROLLADORES ]:\n\n[1] Calcular prioridades\n[2] Cerrar sesión")

        opc = int(input("\n->  "))

        if opc == 1:
            continuarCalcPrioridades = 1
            while continuarCalcPrioridades == 1:
                clear()

                # PUNTAJE Y NÚMERO DE PROYECTO
                listaPuntajes = []

                for proyecto in range(0, 3):
                    clear()
                    semanas = int(input(
                        f'Ingrese la cantidad de semanas para su elaboración (proyecto {proyecto+1}): '))
                    paga = float(
                        input(f'Ingrese cuanto se le va a pagar (proyecto {proyecto+1}): '))
                    modulos = int(
                        input(f'Ingrese la cantidad de módulos (proyecto {proyecto+1}): '))
                    tareas = int(
                        input(f'Ingrese la cantidad de tareas a realizar (proyecto {proyecto+1}): '))


                    puntos = calcular_puntos(semanas, paga, modulos, tareas)

                    listaPuntajes.append(puntos)
                    listaProyectos.append(proyecto)

                for punto in listaPuntajes:
                    for punto2 in range(len(listaPuntajes) - 1):
                        if listaPuntajes[punto2] > listaPuntajes[punto2+1]:
                            listaPuntajes[punto2] = listaPuntajes[punto2+1]
                            listaPuntajes[punto2+1] = listaPuntajes[punto2]

                clear()
                print(listaPuntajes)
                print(
                    f'Órden de prioridades:\n\n1# {listaPuntajes[2]} (proyecto {listaPuntajes[2]})\n2# {listaPuntajes[1][0]} (proyecto {listaPuntajes[1][1]+1})\n3# {listaPuntajes[0][0]} (proyecto {listaPuntajes[0][1]+1})')
                continuarCalcPrioridades = int(
                    input("\n¿Quiere continuar calculando prioridades?\n\n[1] Sí\n[2] No\n\n->  "))

        elif opc == 2:
            cerrar_sesion()

def gerentes():
    continuar = 1

    while continuar == 1 and login != []:
        clear()
        print(
            "\nOpciones:\n\n[1] Calcular prioridades\n[2] Calcular prioridades\n[3] Calcular prioridades\n[4] Calcular prioridades\n[5] Cerrar sesión")

        opc = int(input("\n->  "))

        if opc == 1:
            pass
        elif opc == 5:
            cerrar_sesion()


def recursos_humanos():
    continuar = 1

    while continuar == 1 and login != []:

        clear()
        print(
            "\n[ MENÚ RECURSOS HUMANOS ]:\n\n[1] Ingresar postulantes\n[2] Cerrar sesión")

        opc = int(input("\n->  "))

        if opc == 1:
            clear()
            postulantes = int(input("Ingrese la cantidad de postulantes: "))

            for postulante in range(postulantes):
                clear()
                ocupacion=int(input("Puesto a ocupar: \n[1] Desarrollador \n[2] Administrador \n[3] Control de recursos \n[4] Recursos Humanos\n\n-> "))
                clear()
                telefono=int(input("Ingrese su numero de telefono: "))

                print("\nIngrese los puntajes del 0 al 10: ")

                pProgramacion=int(input("Puntaje en Programacion: "))
                pTrabajoEquipo=int(input("Puntaje en Trabajo en Equipo: "))
                pOrden=int(input("Puntaje de Orden: "))
                pCreatividad=int(input("Puntaje de Creatividad: "))

                cargo=cargo_a_ocupar(pProgramacion,pTrabajoEquipo,pOrden,pCreatividad,telefono,ocupacion)
                if cargo != "":
                    print(f"Se puede ocupar el cargo de {cargo}.")
                else:
                    print("\nNo se puede ocupar el cargo.\n")

                if postulante+1 == postulantes or postulante == postulantes:
                    input("Enter para continuar...")
                    break
                else:
                    ans = int(input("¿Quiere continuar con el otro postulante?\n\n[1] Sí\n[2] No\n\n-> "))

                    if ans == 1:
                        pass
                    else:
                        break
                        break
        elif opc == 2:
            cerrar_sesion()
        

def control_de_recursos():
    pass

# Selector de area por número de area


def areas(area):
    if area == 1:
        sector_administrativo_oficinas()
    elif area == 2:
        sector_administrativo_recepcion()
    elif area == 3:
        desarrolladores()
    elif area == 4:
        gerentes()
    elif area == 5:
        recursos_humanos()
    elif area == 6:
        control_de_recursos()
    else:
        print("Area incorrecta.")


login()