"""
Área de comedor: Dentro de esta área se quiere hacer un control de la entrada y salida
de productos como carne y verdura que entran una cierta cantidad de días. Dentro de
la funcionalidad se informará cuando se hace una compra, se ingresará el consumo de
comida y si se pudre algún alimento.

Además de realizar las funciones, dichas anteriormente, al finalizar el ingreso
de datos se debe informar la cantidad total, si es que sobro, de comida (carne y
verdura).

Pero también se necesita controlar que en ningún momento se quede sin
alguna comida. En caso de suceder se debe informar emitiendo alertas de que se ha
quedado sin algún tipo de comida y los valores nunca pueden ser negativos (como
mínimo 0).
"""

carne = 0
verdura = 0
seguir = "si"


def comprar(cantidad):
    ans = int(input("\nIngrese la cantidad que quiere comprar: "))

    return cantidad+ans, ans


def consumir(cantidad):
    ans = int(input("\nIngrese la cantidad que quiere consumir: "))

    return cantidad+ans, ans


def pudrio(cantidad):
    ans = int(input("\nIngrese la cantidad de productos que se pudrieron: "))

    return cantidad+ans, ans


while seguir == "si":
    print(f'Tienes:\nCarne: {carne} - Verdura: {verdura}')
    opc = int(input(
        "\nAcciones a realizar:\n[1] Comprar\n[2] Consumir\n[3] Se pudrio un alimento\n:"))
    if opc == 1:
        comida = int(input("\nQué quiere comprar?\n[1] Carne\n[2] Verdura\n:"))
        if comida == 1:
            carne, cantidad = comprar(carne)
            print(f'\nCompraste {cantidad} de carne.\n')
        elif comida == 2:
            verdura, cantidad = comprar(verdura)
            print(f'\nCompraste {cantidad} de verdura.\n')
    elif opc == 2:
        pass
    elif opc == 3:
        pass
    else:
        pass

    if carne <= 0 or verdura <= 0:
        print("ALERTA, te has quedado sin algun tipo de comida.")
