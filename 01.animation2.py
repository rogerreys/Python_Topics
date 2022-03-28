import pygame, sys, random
pygame.init()

# VARIABLES
    # Screen size
size = (800, 600)
    # Colors
white = (255,255,255)
red = (255,0,0)
    # Coordenadas
coord_lista = []
for i in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    coord_lista.append([x,y])
    # Time
time= 20

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
# ------ LOGICA

# ------ LOGICA

    screen.fill(white)
# ------ ZONA DIBUJO
    for coor in coord_lista:
        pygame.draw.circle(screen, red, coor, (2)) 
        coor[1]+=1
        if(coor[1]>=598):
            coor[1]=0
            #coor[1]-=1

    

# ------ ZONA DIBUJO
    pygame.display.flip()
    clock.tick(time)