import pygame, sys, random

#VARIABLES
    # Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
     # Size
size = width, hight = 2000, 850

    # Image
#background = pygame.image.load(r"imageBackground/background1.jpg").convert() 
 
# CLASS
class Meteoros(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/meteorito.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y+=1
        if (self.rect.y > hight):
            self.rect.y = -5
            self.rect.x = random.randint(0, width)

class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"imageBackground/spaceship.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]
        pygame.mouse.set_visible(False)

class Game(object):
    def __init__(self):
        self.score = 0
        self.num_meteors = 100
        self.game_over = False
        self.meteor_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()
        # Create Meteors
        for meteor in range(self.num_meteors):
            meteoros = Meteoros()
            meteoros.rect.x = random.randint(0,width)
            meteoros.rect.y = random.randint(0,hight)
            self.meteor_list.add(meteoros)
            self.all_sprite_list.add(meteoros)
        # Add Player
        self.rocket = Rocket()
        self.all_sprite_list.add(self.rocket)
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False
    def run_logic(self):
        if (not self.game_over):
            self.all_sprite_list.update()
            meteor_hit_list = pygame.sprite.spritecollide(self.rocket, self.meteor_list, True)
            for meteor in meteor_hit_list:
                self.score += 1
                print(self.score)
            #if( len(self.meteor_list)<(self.num_meteors) ):
            if( len(self.meteor_list)==0 ):
                print("Game Over")
                self.game_over = True   
    def display_frame(self,screen):
        screen.fill(WHITE)
        if not self.game_over:
            self.all_sprite_list.draw(screen)
        else:
            font = pygame.font.SysFont('Corbel', 35)
            text = font.render("Game Over, Clic to Continue",True,BLACK)
            center_x = (width//2) - (text.get_width()//2)
            center_y = (hight//2) - (text.get_height()//2)
            screen.blit(text, [center_x, center_y])
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    done = False
    # Clock
    clock = pygame.time.Clock()
    game = Game()

    while not done:
        # Events
        done = game.process_events()
        # Logic Game
        game.run_logic()
        # Screen Game
        game.display_frame(screen)
        # Time Game
        clock.tick(60)
    pygame.quit()

# Ejecuta funcion principal
if __name__ == "__main__":
    main()