#Dado un código de caracteres mostrar si coincide con “R2D2”, “C3PO” o “BB8_”.

codigoCaracteres=str(input("Ingrese un código de caracteres:\n"))

if codigoCaracteres == "R2D2":
    print("El código de caracteres coincide con 'R2D2'")
elif codigoCaracteres == "C3PO":
    print("El código de caracteres coincide con 'C3PO'")
elif codigoCaracteres == "BB8_":
    print("El código de caracteres coincide con 'BB8_'")
else:
    print("El código de caracteres no coincide con R2D2, C3PO ni BB8_")