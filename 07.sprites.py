import pygame, sys, random
pygame.init()

#VARIABLES
    # Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

    #Size
size = hight, width = 1024,680
screen = pygame.display.set_mode(size)
    # clock
clock = pygame.time.Clock()
    # Position
position_rocket = []
position_meteor = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()
num_meteors = 50
    # Contadores
score = 0
# IMAGES
background = pygame.image.load(r"imageBackground/background1.jpg").convert()

# METODOS
class Meteors(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/meteorito.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() # Posiciona el sprite
    
    def update(self):
        self.rect.y += 1
        if(self.rect.y > width):
            self.rect.y = -10
            self.rect.x = random.randint(0, hight)

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/spaceship.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect() # Posiciona el sprite
    
    def update(self):
        rocket.rect.x = pygame.mouse.get_pos()[0]
        rocket.rect.y = width-80
        pygame.mouse.set_visible(False)

# Group Meteors
for cont in range(num_meteors):
    meteor = Meteors()
    meteor.rect.x = random.randint(0, hight)
    meteor.rect.y = random.randint(0, width)
    position_meteor.add(meteor)
    all_sprite_list.add(meteor)


rocket = Rocket()
all_sprite_list.add(rocket)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # --- LOGIC
        # Move Meteor & Rocket
    all_sprite_list.update()
        # Detect collition
    blocks_hit_list = pygame.sprite.spritecollide(rocket, position_meteor, True)
    for cont in blocks_hit_list:
        score += 1
        print(score)
    # --- LOGIC


    #screen.fill(WHITE)
    # Background
    screen.blit(background,[0,0])
    # Meteors
    all_sprite_list.draw(screen)
    # Character
   
    pygame.display.flip()
    clock.tick(60)