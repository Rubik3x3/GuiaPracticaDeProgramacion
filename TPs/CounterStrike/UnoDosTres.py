"""
Una empresa de video juegos, EA gomes, nos solicita que realicemos un
programa que simule el juego “Counter Strike 1.5”, donde se nos pide
que programemos algunos de las funcionalidades del juego. Esta
solicitud es enviada para varios programadores. Luego se evaluará cada
proyecto haciendo que los mejores sean incorporados rápidamente a
dicha empresa y además que se destine un presupuesto para la realización del mismo

Los requisitos para que se nos acepte dicho proyecto es que mínimamente cumpla con
lo pedido. Pero el nivel de eficiencia con el que hagamos el programa, ayudara a que se aumente
el presupuesto para su desarrollo.

Funcionalidades:
-------------------------------------------------------------------------------------------------------------
1. Al iniciar la partida el Gamer seleccionará en que equipo quiere estar: “Terrorist” o
“Police”. Ahora según a quien elija tendrá ciertas características particulares: Los
terroristas tienen un aumento de daño de 8 y los “pólice” un aumento en la armadura
de 20.

NOTA 1: el aumento de daño afecta al daño que inflige el arma, la armadura reduce el
daño recibido tanto como el valor de la armadura.

NOTA 2: si se elige “police” nuestro oponente será “terrorist” y viceversa. Esto quiere
decir que las características especiales afectan también a nuestro oponente.
-------------------------------------------------------------------------------------------------------------
2. Al comenzar la ronda el Gamer elegirá cual arma querrá utilizar de la siguiente lista:

a. M4A1: con un daño de 20 por disparo. Por segundo dispara 8 balas.
b. AUG: con un daño de 15 por disparo. Por segundo dispara 5 balas.
c. Scout: con un daño de 45 por disparo. Por segundo dispara2 balas.

Además, el Gamer quiere saber cuántas balas por minuto dispara cada arma junto con
el daño total que puede realizar en un minuto.

NOTA: cuando comienza una ronda la armadura de cada jugador es de 5, la salud de 100
(cantidad máxima que puede tener), el daño que nuestra persona inflige es el del arma
seleccionad. El daño base, que inflige el oponente, es de 40. También el dinero con el que
se comienza es de 500.
-------------------------------------------------------------------------------------------------------------
3. Comienza una nueva ronda y hay ciertas acciones que pueden ocurrir hasta el personaje
muere y es el Gamer quien dirá cuáles son las acciones que lo afectan en el juego:

a. Se le cruza un oponente y dispara: Si el daño infligido en 1 segundo es mayor a
su vida, el oponente muere. Lo que hace que nuestro personaje se cure 10
puntos de vida y que ganemos $300

b. Un oponente le dispara haciéndole un daño. Si el daño (red
ucido con nuestra
armadura), es mayor a nuestra vida, nuestro personaje cae.
c. Rescatar (“police”) o tomar a un rehén(“terrorist”), ambos casos afectan de la
misma manera, lo que nos da $500.

d. Construir trinchera: el jugador puede construir una trinchera para su
protección. La trinchera necesita 30 costales, pero se sabe que el jugador no
puede cargarlos todo de una vez. El jugador agarra X cantidad de costales y los
lleva al lugar donde quiere colocarlos, así sucesivamente hasta haber construido
la trinchera. 

El programa debe decirme cuando la trinchera está construida y si
sobro algún costal de los que llevo ya que pudo haber llevado más de 30 costales
en la suma de cada viaje. Por ultimo también me tiene que decir cuántos viajes
en total hizo nuestro jugador entre la trinchera y el lugar donde estaban los
costales.

Al terminar la ronda me debe decir cuánto dinero ganó y cuantos oponentes mato
NOTA: luego de cada acción, el programa me tiene que decir cuánto tiene de vida nuestro
personaje. OPCIONAL: Tener en cuenta que la cantidad de vida máxima que puede tener
es 100 y la de vida mínima es 0.

Bonus (se puede realizar en un programa distinto):
-------------------------------------------------------------------------------------------------------------
4. Al terminar la partida el Gamer ingresará los scores de TODOS los jugadores, (se sabe
que la cantidad de jugadores por equipo es de 5) y el programa me deberá decir:

a. El score total que se generó en la partida.

b. El score más alto y el score más bajo, el rango entre ellos, junto con sus
respectivas posiciones según el orden ingresado por el Gamer.

c. El score promedio.
-------------------------------------------------------------------------------------------------------------
5. El Gamer ingresa los scores obtenidos en una partida (X rondas) y el programa deberá
decirme, con los lotes formados entre 2 números impares:

a. La productoria de dichos scores, la sumatoria por cada lote.

b. Cuantos valores positivos por cada lote y cuantos lotes hay en total
"""


