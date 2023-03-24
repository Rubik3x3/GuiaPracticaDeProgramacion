"""Dado el saldo en la cuenta bancaria. Se quiere hacer el pago de 4 préstamos de a por
vez y mostrarle a medida que se hace cada pago como va quedando el saldo en la
cuenta."""

saldo=int(input("Ingrese el saldo de la cuenta bancaria:\n"))
saldoRestante = saldo
pagos = [0,0,0,0]
for i in range(4):
    print("Ingrese el pago del prestamo ",i+1)
    pagos[i] = int(input())
    saldoRestante -= pagos[i]
    print("\nEl saldo restante es: $",saldoRestante)