# Plantilla básica para gráficos estáticos con Pygame
# Basada en la estructura de programarcadegames.com

import pygame

# --- Colores (R, G, B) ---
NEGRO   = (  0,   0,   0)
BLANCO  = (255, 255, 255)
ROJO    = (255,   0,   0)
VERDE   = (  0, 255,   0)
AZUL    = (  0,   0, 255)
AMARILLO= (255, 255,   0)
NARANJA = (255, 165,   0)
MORADO  = ( 89,   0, 255)
MARRON  = (128,  73,  34)
CELESTE = (105, 238, 255)
VERDEOSC= ( 11, 102,   9)

# --- Inicialización de Pygame ---
pygame.init()

# --- Tamaño de la ventana ---
ANCHO = 700
ALTO  = 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# --- Título de la ventana ---
pygame.display.set_caption("Casa")

# --- Bucle principal ---
hecho = False
reloj = pygame.time.Clock()

while not hecho:

    # 1) Gestión de eventos (no modificar)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # 2) Fondo de la pantalla
    pantalla.fill(BLANCO)

    # -------------------------------------------------------
    # 3) DIBUJA AQUÍ TUS FIGURAS
    # -------------------------------------------------------

    # Línea: pygame.draw.line(pantalla, color, [x1, y1], [x2, y2], grosor)
    # Rectángulo: pygame.draw.rect(pantalla, color, [x, y, ancho, alto], grosor)
    #   grosor=0 → relleno; grosor>0 → solo borde
    # Elipse / círculo: pygame.draw.ellipse(pantalla, color, [x, y, ancho, alto], grosor)
    # Polígono: pygame.draw.polygon(pantalla, color, [[x1,y1],[x2,y2],...], grosor)
    # Arco: pygame.draw.arc(pantalla, color, [x, y, ancho, alto], ang_inicio, ang_fin, grosor)
    #   ángulos en radianes; 0 = derecha, math.pi/2 = arriba
    import math

    pygame.draw.rect(pantalla, CELESTE, [0, 0, 700, 500], 0)
    pygame.draw.rect(pantalla, VERDEOSC, [0, 300, 700, 200], 0)
    pygame.draw.ellipse(pantalla, AMARILLO, [600, -100, 200, 200], 0)
    pygame.draw.rect(pantalla, MORADO, [100, 128, 250, 200], 0)
    pygame.draw.rect(pantalla, MARRON, [128, 41, 50, 80], 0)
    pygame.draw.polygon(pantalla, AMARILLO, [[50,128],[225,50],[400,128]], 0)
    pygame.draw.rect(pantalla, CELESTE, [128, 156, 50, 50], 0)
    pygame.draw.rect(pantalla, MARRON, [275, 250, 50, 78], 0)
    pygame.draw.polygon(pantalla, VERDE, [[275,328],[375,400],[425,400],[325,328]], 0)
    pygame.draw.rect(pantalla, VERDE, [0, 380, 700, 35], 0)
    





    

    # Texto en pantalla
    fuente = pygame.font.SysFont("Arial", 24)
    texto  = fuente.render("", True, NEGRO)
    pantalla.blit(texto, [50, 350])

    # -------------------------------------------------------
    # 4) Actualizar pantalla (no modificar)
    # -------------------------------------------------------
    pygame.display.flip()
    reloj.tick(60)

# --- Salir de Pygame ---
pygame.quit()
