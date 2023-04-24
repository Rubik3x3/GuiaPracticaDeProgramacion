
scores = []  # Scores
scoreMax = [0, 1]  # [Score,Posicion]
scoreMin = [0, 1]  # [Score,Posicion]
totalScores = 0  # Suma de todos los scores

for i in range(10):
    if i < 5:
        print("Ingrese el score ", i+1, " de los policias: ", end="", sep="")
    else:
        print("Ingrese el score ", i-4, " de los terroristas: ", end="", sep="")

    score = int(input())
    scores.append(score)

    if i == 0:
        scoreMax[0] = score
        scoreMin[0] = score
    else:
        if scoreMax[0] < score:
            scoreMax[0] = score
            scoreMax[1] = i+1  # Posicion
        if scoreMin[0] > score:
            scoreMin[0] = score
            scoreMin[1] = i+1  # Posicion

    totalScores += score

# Calcular promedio
promedioScores = totalScores/10
# Rango
diferenciaScores = scoreMax[0]-scoreMin[0]

# Mostrar los datos
print("Todos los scores: ", scores, sep="")
print("Score más alto: ", scoreMax[0], " número: ", scoreMax[1], sep="")
print("Score más bajo: ", scoreMin[0], " número: ", scoreMin[1], sep="")
print("Rango: ", diferenciaScores, sep="")
print("Promedio Scores: ", promedioScores, sep="")
