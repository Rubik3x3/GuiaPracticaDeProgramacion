"""
Lucha Básica. El juego será acerca de un luchador que debe vencer a su oponente. Al
luchar, el jugador puede usar dos diferentes ataques, una patada (daño de 15) o un
puñetazo (daño de 10).
La lucha termina cuando terminen las X cantidad de turnos o cuanto el
oponente caiga. La vida del oponente se carga antes de comenzar la lucha. Luego de la
lucha se evaluará:
 Si la vida del oponente llega a una cantidad mayor a -10, pero menor o igual a
0, el jugador ganará.
 Si la vida del oponente llega por debajo de -10, este será dañado de una
forma grave, y el jugador perderá.
 Si la vida del oponente no llega a 0 en menos de X turnos, el jugador perderá.
"""