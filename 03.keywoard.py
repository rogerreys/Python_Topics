import pygame, sys, random
pygame.init()

# Variables 
    # Size
size = (800, 600)
    # Color
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (250, 0, 0)

    # Position
coor_x = 100
coor_y = 100
    # Speed
speed = 3

screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # METODO 1
        #if event.type == pygame.KEYUP:
        #    if(event.key == pygame.K_UP): speed = 0
        #    if(event.key == pygame.K_DOWN): speed = 0
        #    if(event.key == pygame.K_LEFT): speed = 0
        #    if(event.key == pygame.K_RIGHT): speed = 0
        #if event.type == pygame.KEYDOWN:
        #    if(event.key == pygame.K_UP): speed = 2
        #    if(event.key == pygame.K_DOWN): speed = -2
        #    if(event.key == pygame.K_LEFT): speed = -2
        #    if(event.key == pygame.K_RIGHT): speed = 2
    
    #coor_y += speed
    #coor_x += speed
    #---- Logic
        # METODO 2
        # Key
    if pygame.key.get_pressed()[pygame.K_UP]: coor_y -= speed
    if pygame.key.get_pressed()[pygame.K_DOWN]: coor_y += speed
    if pygame.key.get_pressed()[pygame.K_LEFT]: coor_x -= speed
    if pygame.key.get_pressed()[pygame.K_RIGHT]:coor_x += speed
        # Limit Windows
    if(coor_x >= 790):coor_x -= speed
    if(coor_x <= 10): coor_x += speed
    if(coor_y >= 590):coor_y -= speed
    if(coor_y <= 10): coor_y += speed
        # Change color
    
    #---- Logic

    screen.fill(WHITE)
    #---- Zona Graphic

    #pygame.draw.rect(screen, RED, (coor_x, coor_y, 50, 50))
    pygame.draw.circle(screen, RED, (coor_x, coor_y), 10)
    #---- Zona Graphic
    pygame.display.flip()