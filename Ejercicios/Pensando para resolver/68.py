#Dado un numero devolver su factorial.

num = int(input("Ingrese un número para calcular su factorial: "))

factorial = 0
if num >= 0:
    if num != 1 and num != 0:
        for i in range(num,1,-1):
            if i == num:
                factorial = num
            else:
                factorial *= i
    else:
        factorial = 1
    print(factorial)
else:
    print("Ingrese un número mayor que 0.")
    exit()



