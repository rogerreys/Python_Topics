import pygame, sys

# Variables

# Screen
size = high, width = 800, 600
screen = pygame.display.set_mode(size)
# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Time
clock = pygame.time.Clock()
# Image Background
background = pygame.image.load(r"imageBackground/background1.jpg").convert()
player = pygame.image.load(r"imageBackground/spaceship.png").convert()
# Clear Background White
player.set_colorkey(WHITE)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # LOGIC
    posicion = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    # LOGIC
        

    #screen.fill(WHITE)
    screen.blit(background, [0,0])
    screen.blit(player, posicion)
    pygame.display.flip() 
    clock.tick(60)
