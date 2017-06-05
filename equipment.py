class Paddle(object):
    def __init__(self, x_position, y_position, width, height, screen_height, speed=5):
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.screen_height = screen_height
        self.speed = speed

    def move_up(self):   
        if self.y_position - self.speed >= 0:
            self.y_position -= self.speed
        else:
            self.y_position = 0

    def move_down(self): 
        if self.y_position + self.height + self.speed <= self.screen_height :
            self.y_position += self.speed
        else:
            self.y_position = self.screen_height - self.height

class Ball(object):
    def __init__(self, x_position, y_position, x_direction, y_direction, size, screen_height, speed=5):
        self.x_position = x_position
        self.y_position = y_position
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.size = size
        self.screen_height = screen_height
        self.speed = speed

    def change_direction_if_collided(self, paddle1, paddle2):

        #The actual location of the paddle is the north-western point of the rectangle 
        #Therefor, when checking for collision, one must take into consideration the height and width of the rectangle
        
        ####Paddle1 Collision####
        paddle1_x_collision = self.x_position == paddle1.x_position + paddle1.width
        paddle1_y_collision = self.y_position >= paddle1.y_position - self.size and self.y_position <= paddle1.y_position + paddle1.height
        paddle1_collision = paddle1_x_collision and paddle1_y_collision  

        ####Paddle2 Collision####
        paddle2_x_collision = self.x_position >= paddle2.x_position - self.size
        paddle2_y_collision = self.y_position >= paddle2.y_position - self.size and self.y_position <= paddle2.y_position + paddle2.height
        paddle2_collision = paddle2_x_collision and paddle2_y_collision 

        if paddle1_collision or paddle2_collision:
            self.x_direction *= -1 #switches direction from whatever it was before. 

        top_wall_collision = self.y_position <= 0
        bottom_wall_collision = self.y_position + self.size >= self.screen_height

        if top_wall_collision or bottom_wall_collision:
            self.y_direction *= -1

    def move(self):
        self.x_position += self.speed * self.x_direction
        self.y_position += self.speed * self.y_direction 


    def goes_off_an_edge(self, paddle1, paddle2):
        player_1_lost = self.x_position < paddle1.x_position + paddle1.width
        player_2_lost = self.x_position > paddle2.x_position - self.size
        
        if player_1_lost or player_2_lost: 
            return True

        




        '''
        #Losing the game
        if ball_x_position < 30: done = True
        if ball_x_position > p2_x_position+10: done = True
        '''
        

                                  