"""
Al terminar la partida el Gamer ingresará los scores de TODOS los jugadores, (se sabe
que la cantidad de jugadores por equipo es de 5) y el programa me deberá decir:
a. El score total que se generó en la partida.
b. El score más alto y el score más bajo, el rango entre ellos, junto con sus
respectivas posiciones según el orden ingresado por el Gamer.
c. El score promedio.
"""

scoreMax = 0
scoreMaxPos = 1
scoreMaxEq = ""

scoreMin = 0
scoreMinPos = 1
scoreMaxEq = ""

totalScores = 0  

for i in range(10):
    if i < 5:
        print("Ingrese el score ", i+1, " de los policias: ", end="", sep="")
    else:
        print("Ingrese el score ", i-4, " de los terroristas: ", end="", sep="")

    score = int(input())

    if i == 0:
        scoreMax = score
        scoreMin = score

        scoreMaxEq = "Policia"
        scoreMinEq = "Policia"
    else:
        if scoreMax < score:
            scoreMax = score
            scoreMaxPos = i+1 

            if i < 5:
                scoreMaxEq = "Policia"
            else:
                scoreMaxEq = "Terrorista"

        if scoreMin > score:
            scoreMin = score
            scoreMinPos = i+1 

            if i < 5:
                scoreMinEq = "Policia"
            else:
                scoreMinEq = "Terrorista"

    totalScores += score

promedioScores = totalScores/10
diferenciaScores = scoreMax-scoreMin
 
#print("Todos los scores: ", scores, sep="")
print("Score más alto: ", scoreMax, " jugador: ", scoreMaxPos, " equipo: ", scoreMaxEq, sep="")
print("Score más bajo: ", scoreMin, " jugador: ", scoreMinPos, " equipo: ", scoreMinEq, sep="")
print("Rango: ", diferenciaScores, sep="")
print("Promedio Scores: ", promedioScores, sep="")
