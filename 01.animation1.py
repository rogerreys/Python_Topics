import pygame, sys
pygame.init()
# Color
BLACK = (0 , 0 , 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Animacion
    # Coordenadas
coord_x, coord_y = 10, 10
    # Velocidad
speed_x, speed_y = 1, 3

# Size screem
size = (800, 600)
screen = pygame.display.set_mode(size)

# Time game, Controla los FPS
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT: sys.exit()
    # ----- LOGICA
    if (coord_x >= 750 or coord_x  < 0 ):
        speed_x *= -1
    if (coord_y >= 550 or coord_y  < 0 ):
        speed_y *= -1
    
    coord_y += speed_y
    coord_x += speed_x
    # ----- LOGICA
    
    # Pintar pantalla
    screen.fill(WHITE)
    
    # ---ZONA DE DIBUJO
    pygame.draw.rect(screen, RED, (coord_x, coord_y, 50, 50))

        # FIGURAS 
    #for x in range(100, 500,100):
    #    pygame.draw.rect(screen, BLACK, (x,230, 50, 50))
    #    pygame.draw.line(screen, GREEN, [x,10], [x, 90], 9)
    #pygame.draw.line(screen, RED, [50,200],[80,100],5)
    #pygame.draw.ellipse(screen, BLUE,  [300, 300, 30, 45],1)
    #pygame.draw.circle(screen, GREEN, (100,100),(90))

    # ---ZONA DE DIBUJO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(80)