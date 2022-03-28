import pygame, sys
pygame.init()

# VARIABLES
    # Size
size = width, hight = 1500, 800
    # Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
    # Dimesiones Barras
rec_dim_a = 10
rec_dim_h = 200
    # Dimensiones Ball
radioBall = 20
    # Coordenas Player
coor_y_p1 = 30
coor_y_p2 = 30
    # Coordenas Ball
coor_x_ball = 100
coor_y_ball = 100
    # Posicion
#posicion1 = (10, coor_y_p1, rec_dim_a, rec_dim_h)
#sposicion2 = (780, coor_y_p1, rec_dim_a, rec_dim_h)
    # Speed
speed_players = 10
speed_ball_x = 4
speed_ball_y = 4
    # Score
score_player1 = 0
score_player2 = 0
    # Screem
screem = pygame.display.set_mode(size)
    # Clock
clock = pygame.time.Clock()


# EJECUCION
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ---- LOGIC
        # ---- Move Player 1
    if (pygame.key.get_pressed()[pygame.K_w]): coor_y_p1 -= speed_players
    if (pygame.key.get_pressed()[pygame.K_s]): coor_y_p1 += speed_players
        # ---- Move Player 2
    if (pygame.key.get_pressed()[pygame.K_UP]): coor_y_p2 -= speed_players
    if (pygame.key.get_pressed()[pygame.K_DOWN]): coor_y_p2 += speed_players
        # ---- Move Ball
    coor_y_ball += speed_ball_y
    coor_x_ball += speed_ball_x

        # ---- Limit Players
    if( coor_y_p1 >= (hight-rec_dim_h) ): coor_y_p1 -= speed_players
    if( coor_y_p2 >= (hight-rec_dim_h) ): coor_y_p2 -= speed_players
    if( coor_y_p1 < 0 ): coor_y_p1 += speed_players
    if( coor_y_p2 < 0 ): coor_y_p2 += speed_players
        # ---- Limit Ball y
    if( coor_y_ball < 0 or coor_y_ball >= hight ): speed_ball_y *= -1
        # ---- If ball exit
    if(coor_x_ball>width or coor_x_ball < 0): 
        if(coor_x_ball>width):
            score_player1 += 1
            print(f"score_player1: {score_player1}")

            
        if(coor_x_ball< 0):
            score_player2 += 1
            print(f"score_player2: {score_player2}")
            
        coor_y_ball = 300
        coor_x_ball = 400
        speed_ball_x *= -1

    # ---- LOGIC

    # Print Screen
    screem.fill(BLACK)

    font_player1 = pygame.font.SysFont('Corbel', 100)
    text_player1 = font_player1.render(str(score_player1), True, WHITE)
    left_text_player1_x = (width//4) - (text_player1.get_width()//2)
    left_text_player1_y = (text_player1.get_height()) - (text_player1.get_height()//3)
    screem.blit(text_player1, [left_text_player1_x,left_text_player1_y])

    font_player2 = pygame.font.SysFont('Corbel', 100)
    text_player2 = font_player2.render(str(score_player2), True, WHITE)
    left_text_player2_x = width - (width//4) - (text_player1.get_width()//2)
    left_text_player2_y = (text_player1.get_height()) - (text_player1.get_height()//3)
    screem.blit(text_player2, [left_text_player2_x,left_text_player2_y])
    
    # ---- ZONA GRAPHIC
        # Player 1
    player1 = pygame.draw.rect(screem, WHITE, (10, coor_y_p1, rec_dim_a, rec_dim_h))
        # Player 2
    player2 = pygame.draw.rect(screem, WHITE, (width-20, coor_y_p2, rec_dim_a, rec_dim_h))
        # Ball
    ball = pygame.draw.circle(screem, RED, (coor_x_ball, coor_y_ball), radioBall)
    # ---- ZONA GRAPHIC
    
    # ---- COLISIONES
    if(player1.colliderect(ball) or player2.colliderect(ball)): speed_ball_x *= -1

    pygame.display.flip()
    clock.tick(120)