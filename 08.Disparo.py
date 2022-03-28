import pygame, sys, random
pygame.init()

#VARIABLES
    # Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
    # Size
size = width, hight = 1024, 680
screen = pygame.display.set_mode(size)
    # Clock
clock = pygame.time.Clock()
    # Ṕosicion
posicionRocket_x = 100
    # Speed Rocket
speedRocket = 10

    # Sprite Group
all_sprite_list = pygame.sprite.Group()
meteoritos_list = pygame.sprite.Group()
balas_list = pygame.sprite.Group()
    # Cantidad
num_meteors = 50
score = 0
    # Image
background = pygame.image.load(r"imageBackground/background1.jpg") 
 
# CLASS
class Meteoros(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/meteorito.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/spaceship.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0
    def changeSpeed(self,x):
        self.speed_x += x 
    def update(self):
        self.rect.x = self.speed_x
        self.rect.y = hight-60
        

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/bala.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 2


# CALL CLASS
rocket = Rocket()
all_sprite_list.add(rocket)

#all_sprite_list.add(bala)


# Position Meteor
for pos in range(num_meteors):
    meteoros = Meteoros()
    meteoros.rect.x = random.randint(0,width)
    meteoros.rect.y = random.randint(0,hight-150)
    meteoritos_list.add(meteoros)
    all_sprite_list.add(meteoros)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
        #    bala = Bala()
        #    bala.rect.x = pygame.mouse.get_pos()[0]+10
        #    bala.rect.y = rocket.rect.y 
        #    all_sprite_list.add(bala)
        #    balas_list.add(bala)
        # Move Bala
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                bala = Bala()
                bala.rect.x = rocket.rect.x
                bala.rect.y = rocket.rect.y
                all_sprite_list.add(bala)
                balas_list.add(bala)
    # Move Rocket
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        rocket.changeSpeed(-speedRocket)
        if rocket.rect.x < 0: rocket.changeSpeed(+speedRocket)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        rocket.changeSpeed(speedRocket)
        if rocket.rect.x > width-50: rocket.changeSpeed(-speedRocket)
        
        
        # Colition
        for bal in balas_list:
            blocks_hit_list = pygame.sprite.spritecollide(bal, meteoritos_list, True)
            for meteor in blocks_hit_list:
                all_sprite_list.remove(bal)
                balas_list.remove(bal)
                score +=1
                print(score)
            if bal.rect.y < -10:
                all_sprite_list.remove(bal)
                balas_list.remove(bal)


    # Call clase
    all_sprite_list.update()
    
    
    # Screen
        # Background
    screen.blit(background, [0,0])
        # Sprite group
    all_sprite_list.draw(screen)
     
    
    pygame.display.flip()
    
    clock.tick(60)