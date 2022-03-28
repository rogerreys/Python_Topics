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

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #screen.fill(WHITE)
    screen.blit(background, [0,0])
    pygame.display.flip() 
    clock.tick(60)
