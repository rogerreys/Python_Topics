import sys, pygame
# Initializes each of these modules
pygame.init()

size = width, height = 1024, 720
speed = [1, 1]
black = 0, 0, 0
# create a graphical window
screen = pygame.display.set_mode(size)
# we load our ball image.
ball = pygame.image.load("ball.png")
# Rect - rectangular area.
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        # exit the program
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
