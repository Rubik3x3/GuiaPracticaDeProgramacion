"""Realizar un programa que permita ingresar 2 números, A y B por ejemplo, y nos muestra 
cuanto es el A% de B. Por ejemplo: Se ingresan 40 y 50. Haciendo el cálculo nos daría que el 40% de 50 es 20."""

num1=int(input("Ingrese el número 1:\n"))
num2=int(input("Ingrese el número 2:\n"))

resultado=(num1*num2)/100

print("El ",num1,"% ","de ",num2," es: ",resultado)