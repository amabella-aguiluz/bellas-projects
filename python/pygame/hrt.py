import pygame
import os
import random

    # initializing game #
screen = pygame.display.set_mode((800, 600)) # set screen size (width, height)
clock = pygame.time.Clock() # set fps
velocity = 2 # speed of horse
running = True # keep game loop running
maze_image = pygame.image.load("assets/map_test.png").convert()  # convert for faster pixel access
maze_mask = pygame.mask.from_threshold(maze_image, (0, 0, 0), (10, 10, 10)) #convert maze png to mask
v_temp1 = random.choice([-1, 1]) * velocity
v_temp2 = random.choice([-1, 1]) * velocity
    # initializing game #

    # initialize horse
class Horse:
    def __init__(self, x, y, image_path, velocity_x, velocity_y):
        self.x = x # starting x position
        self.y = y # starting y position
        self.velocity_x = v_temp1 # velocity direction x
        self.velocity_y = v_temp2 # velocity direction y
        self.image = pygame.image.load(image_path).convert_alpha() #load image
        self.rect = self.image.get_rect(center =(x, y))

    def draw(self, surface): # display self
        surface.blit(self.image, self.rect)
    # initialize horse

def when_bounced(x, y):
    x *= 5
    y *= 5
    return 

def horse_bounce(horse):
    if(horse.rect.left < 0): #hits left
        horse.velocity_x = 1
        when_bounced(horse.velocity_x, horse.velocity_y)
    elif(horse.rect.right > 800): # hits right
        horse.velocity_x = -1
        when_bounced(horse.velocity_x, horse.velocity_y)
    elif(horse.rect.top < 0): # hits top
        horse.velocity_y = 1
        when_bounced(horse.velocity_x, horse.velocity_y)
    elif(horse.rect.bottom > 600): # hits bottom
        horse.velocity_y = -1
        when_bounced(horse.velocity_x, horse.velocity_y)

def move_horse(horse):
    horse.x += horse.velocity_x
    horse.y += horse.velocity_y
    horse_bounce(horse)
    horse.rect.center = (horse.x, horse.y)

horse1 = Horse(100, 100, "assets/horse_1.png", v_temp1, v_temp2) # <-- place horse

    # gui open #
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
    # gui open #
    