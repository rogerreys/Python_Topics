import pygame, sys
pygame.init()
# Variables
    # Size
size = (800, 600)
    # Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
    # Time
clock = pygame.time.Clock()


screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #----LOGIC
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    pygame.mouse.set_visible(False)

    #----LOGIC
    screen.fill(WHITE)
    #----ZONAL GRAFIC
    pygame.draw.circle(screen, GREEN, (x,y), (9))

    #----ZONAL GRAFIC

    pygame.display.flip()
    clock.tick(60)