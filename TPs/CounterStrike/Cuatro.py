scores = []  # Scores
scoreMax = [0, 1,""]  # [Score,Posicion,Equipo]
scoreMin = [0, 1,""]  # [Score,Posicion,Equipo]
totalScores = 0  # Suma de todos los scores

def verEquipo(numero):
    if numero < 5:
        return "Policia"
    else:
        return "Terrorista"

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
        scoreMax[2] = "Policia"
        scoreMin[2] = "Policia"
    else:
        if scoreMax[0] < score:
            scoreMax[0] = score
            scoreMax[1] = i+1  # Posicion
            scoreMax[2] = verEquipo(i)
        if scoreMin[0] > score:
            scoreMin[0] = score
            scoreMin[1] = i+1  # Posicion
            scoreMin[2] = verEquipo(i)

    totalScores += score

# Calcular promedio
promedioScores = totalScores/10
diferenciaScores = scoreMax[0]-scoreMin[0]

# Mostrar los datos
print("Todos los scores: ", scores, sep="")
print("Score más alto: ", scoreMax[0], " jugador: ", scoreMax[1], " equipo: ", scoreMax[2], sep="")
print("Score más bajo: ", scoreMin[0], " jugador: ", scoreMin[1], " equipo: ", scoreMin[2], sep="")
print("Rango: ", diferenciaScores, sep="")
print("Promedio Scores: ", promedioScores, sep="")
