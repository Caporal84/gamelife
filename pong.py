import pygame
import random

# define las dimensiones de la ventana
ancho_ventana = 640
alto_ventana = 480

# define las dimensiones de las paletas y la pelota
ancho_paleta = 20
alto_paleta = 80
diametro_pelota = 20

# define la velocidad de las paletas y la pelota
velocidad_paleta = 5
velocidad_pelota = 5

# define los colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# inicializa Pygame
pygame.init()

# crea la ventana
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Pong")

# crea las paletas y la pelota
paleta_1 = pygame.Rect(0, alto_ventana / 2 - alto_paleta / 2, ancho_paleta, alto_paleta)
paleta_2 = pygame.Rect(ancho_ventana - ancho_paleta, alto_ventana / 2 - alto_paleta / 2, ancho_paleta, alto_paleta)
pelota = pygame.Rect(ancho_ventana / 2 - diametro_pelota / 2, alto_ventana / 2 - diametro_pelota / 2, diametro_pelota, diametro_pelota)

# establece la dirección inicial de la pelota de forma aleatoria
direccion_pelota = [random.choice([-1, 1]), random.choice([-1, 1])]

# define una función para dibujar el mundo
def dibujar_mundo():
    ventana.fill(negro)
    pygame.draw.rect(ventana, blanco, paleta_1)
    pygame.draw.rect(ventana, blanco, paleta_2)
    pygame.draw.ellipse(ventana, blanco, pelota)

# define una función para mover las paletas
def mover_paletas():
    teclas_pulsadas = pygame.key.get_pressed()
    if teclas_pulsadas[pygame.K_w] and paleta_1.top > 0:
        paleta_1.move_ip(0, -velocidad_paleta)
    if teclas_pulsadas[pygame.K_s] and paleta_1.bottom < alto_ventana:
        paleta_1.move_ip(0, velocidad_paleta)
    if teclas_pulsadas[pygame.K_UP] and paleta_2.top > 0:
        paleta_2.move_ip(0, -velocidad_paleta)
    if teclas_pulsadas[pygame.K_DOWN] and paleta_2.bottom < alto_ventana:
        paleta_2.move_ip(0, velocidad_paleta)

# define una función para mover la pelota
def mover_pelota():
    pelota.move_ip(velocidad_pelota * direccion_pelota[0], velocidad_pelota * direccion_pelota[1])
    if pelota.left < 0 or pelota.right > ancho_ventana:
        direccion_pelota[0] = -direccion_pelota[0]
    if pelota.top < 0 or pelota.bottom > alto_vent
