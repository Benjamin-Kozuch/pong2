import pygame
import equipment #this equipment bag contains all the equipment needed for the game
pygame.init()

#Makes a black screen pop-up
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))  

#Need this to change the FPS (frames per second) later.
clock = pygame.time.Clock()

#create equipment for the game (ball and paddles)
player_1 = equipment.Paddle(30,screen_height/2, 10, 60, screen_height, 5) 
player_2 = equipment.Paddle(screen_width - 40, screen_height/2, 10, 60, screen_height, 5)
ball_1 = equipment.Ball(screen_width / 2,screen_height / 2,-1,1,10,screen_height,5) 

#Game Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Move p1 paddle up or down
    if pygame.key.get_pressed()[pygame.K_a]: 
        player_1.move_up()
    if pygame.key.get_pressed()[pygame.K_z]: 
        player_1.move_down()

    #Move p2 paddle up or down
    if pygame.key.get_pressed()[pygame.K_UP]:
        player_2.move_up()
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        player_2.move_down()

    ball_1.move()
    
    ball_1.change_direction_if_collided(player_1,player_2)
    if ball_1.goes_off_an_edge(player_1,player_2): done = True

    #without this the moving around square would leave a trailing tail.
    screen.fill((255, 255, 255)) 

    #Draw Ball
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(ball_1.x_position, ball_1.y_position, ball_1.size, ball_1.size))
    
    #Draw Player1 Paddle
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(player_1.x_position, player_1.y_position, player_1.width, player_1.height))
    
    #Draw Player2 Paddle
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(player_2.x_position, player_2.y_position, player_2.width, player_2.height))

    pygame.display.flip()
    
    clock.tick(120)


