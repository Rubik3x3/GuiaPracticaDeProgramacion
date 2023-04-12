

"""Dado el saldo en la cuenta bancaria. Se quiere hacer una transferencia. Para ello se
debe ingresar el monto, el nombre y apellido del destinatario. Se le debe mostrar el
estado de la cuenta luego de la trasferencia como así el nombre del propietario de la
cuenta y el nombre de a quien se le hizo la transferencia."""

saldo=int(input("Ingrese el saldo de la cuenta bancaria:\n"))
nombreP=str(input("Ingrese nombre y apellido del propietario:\n"))

monto=int(input("Ingrese el monto a transferir:\n"))
nombreD=str(input("Ingrese nombre y apellido del destinatario:\n"))

saldoRestante=saldo-monto

print("\nTransferencia:\n\nDestinatario: ",nombreD,"\nMonto: $",monto,"\nPropietario: ",nombreP,"\n\nSaldo luego de la transferencia: $",saldoRestante)