#EVALUACIÓN DE COMPUTACIÓN - Franco Talarico - 29/03/2023

#Problema:
"""
Este sistema gestionará las compras de un almacen.
El usuario cargara el producto, la cantidad y el precio base del mismo.
Se aclara que solo se compran como maximo dos productos distintos.
Al precio base de cada producto se le aplicara un IVA del 14%.
Se deberá mostrar el total de la compra y el vuelto que se debe dar,
habiendole pedido el monto con el que abona.
"""

total = 0

for i in range(2):
    precioFinal = 0

    print("Ingrese el producto ",i+1)
    producto = str(input())

    print("Ingrese el precio base del producto ",i+1)
    precioBase = int(input())

    print("Ingrese la cantidad de productos",i+1)
    cantidad = int(input())

    precioIVA = precioBase+((precioBase*14)/100)

    if cantidad >= 3 and cantidad <= 7:
        precioFinal = precioIVA - ((precioIVA*7)/100)
    else:
        precioFinal = precioIVA

    total += (precioFinal * cantidad)

print("El precio total es de: $",total)
monto = int(input("Ingrese el monto con el que va a pagar: $"))
vuelto = monto-total
print("Tu vuelto es de $",vuelto)