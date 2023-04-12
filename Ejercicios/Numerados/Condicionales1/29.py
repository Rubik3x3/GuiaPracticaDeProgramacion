"""Se toma una muestra de sangre para hacer un test de VIH rápido. 
De ello se ingresa si se detectaron anticuerpos y hace cuantos 
días fue la exposición al contagio. 
Se puede afirmar, casi en un 100%, que la persona tiene VIH si: 
se detectaron anticuerpos y la cantidad de días es mayor a 30."""

anticuerpos=str(input("Ingrese si se detectaron anticuerpos [Si/No]:\n"))
dias=int(input("Ingrese cuantos días fue la exposición al contagio:\n"))

if anticuerpos == "Si" and dias > 30:
    print("La persona tiene VIH.")
else:
    print("La persona no tiene VIH.")