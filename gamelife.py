import random
import time
import os

# dimensiones del mundo
filas = 50
columnas = 50

# crea una matriz de ceros para representar el mundo
mundo = [[0 for x in range(columnas)] for y in range(filas)]

# inicializa el mundo con células vivas de forma aleatoria
for i in range(filas):
    for j in range(columnas):
        if random.random() > 0.5:
            mundo[i][j] = 1

# define una función para imprimir el mundo en la consola
def imprimir_mundo():
    os.system('clear')
    for i in range(filas):
        for j in range(columnas):
            if mundo[i][j] == 0:
                print(".", end="")
            else:
                print("#", end="")
        print()
    time.sleep(0.1)

# define una función para calcular el estado siguiente del mundo
def calcular_siguiente_estado():
    nuevo_mundo = [[0 for x in range(columnas)] for y in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            # cuenta el número de vecinos vivos
            vecinos_vivos = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    fila_vecino = (i + x + filas) % filas
                    columna_vecino = (j + y + columnas) % columnas
                    vecinos_vivos += mundo[fila_vecino][columna_vecino]

            # aplica las reglas del juego
            if mundo[i][j] == 1 and (vecinos_vivos == 3 or vecinos_vivos == 4):
                nuevo_mundo[i][j] = 1
            elif mundo[i][j] == 0 and vecinos_vivos == 3:
                nuevo_mundo[i][j] = 1

    # actualiza el mundo con el nuevo estado
    for i in range(filas):
        for j in range(columnas):
            mundo[i][j] = nuevo_mundo[i][j]

# ejecuta el juego
while True:
    imprimir_mundo()
    calcular_siguiente_estado()
