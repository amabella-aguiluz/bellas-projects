import pygame
import os
import random

    ######## initializing game ########

screen = pygame.display.set_mode((800, 600)) # set screen size (width, height)
clock = pygame.time.Clock() # set fps
velocity = 1.1 # speed of horse
running = True # keep game loop running
    #-- mask
maze_image = pygame.image.load("assets/map_test.png").convert()  # convert for faster pixel access
maze_mask = pygame.mask.from_threshold(maze_image, (0, 0, 0), (10, 10, 10)) #convert maze png to mask
    #-- mask
    #-- velocity
v_temp1 = random.choice([-1, 1]) * velocity
v_temp2 = random.choice([-1, 1]) * velocity
    #-- velocity

    ######## initializing game ########


    # initialize horse object
class Horse:
    def __init__(self, name, x, y, image_path, velocity_x, velocity_y):
        self.name = ""
        self.x = x # starting x position
        self.y = y # starting y position
        self.velocity_x = v_temp1 # velocity direction x
        self.velocity_y = v_temp2 # velocity direction y
        self.image = pygame.image.load(image_path).convert_alpha() #load image
        self.rect = self.image.get_rect(center =(x, y))

    def draw(self, surface): # display self
        surface.blit(self.image, self.rect)
    # initialize horse object

def when_bounced(horse):
    horse.velocity_x *= 1.0001
    horse.velocity_y *= 1.0001
    return horse

def horse_bounce(horse):
    if(horse.rect.left < 0 or horse.rect.right > 800): # hits left or right
        horse.velocity_x *= -1
    elif(horse.rect.top < 0 or horse.rect.bottom > 600): # hits top or bottom
        horse.velocity_y *= -1
    when_bounced(horse)

def move_horse(horse):
    #horse_bounce(horse)
    bounce_wall(horse)
    horse.x += horse.velocity_x
    horse.y += horse.velocity_y
    horse.rect.center = (horse.x, horse.y)

# bounce against walls
def bounce_wall(horse):
    next_x = int(horse.x + horse.velocity_x)
    next_y = int(horse.y + horse.velocity_y)

    if maze_mask.get_at((next_x, next_y)):  
        horse.velocity_x *= random.uniform(0.85, 1.15)  # random adjustment to x
        horse.velocity_y *= random.uniform(0.85, 1.15)  # random adjustment to y velocity

        # reverse velocity
        if maze_mask.get_at((int(horse.x), next_y)):  # hits left or right
            horse.velocity_x *= -1 
        if maze_mask.get_at((next_x, int(horse.y))):  #hits top or bottom
            horse.velocity_y *= -1  
    when_bounced(horse)


    ######## create horses  ########
horse1 = Horse("Horse 1", 100, 100, "assets/horse_1.png", v_temp1, v_temp2) # <-- place horse
    ######## create horses  ########


    ######## gui open ########
while running: 
    clock.tick(60) # <-- set fps 60

    move_horse(horse1)

# for loop through the event queue 
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:  #<-- Check for QUIT event   
            running = False

    screen.blit(maze_image, (0, 0))  # <-- draw maze map
    horse1.draw(screen)  # <-- draw horses here (if any)

    pygame.display.flip()  # <-- refresh screen
    ######## gui open ########
    