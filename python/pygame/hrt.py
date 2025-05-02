import pygame
import os
import random
import math

    ######## initializing game ########

screen = pygame.display.set_mode((800, 600)) # set screen size (width, height)
clock = pygame.time.Clock() # set fps
velocity = 1 # speed of horse
running = True # keep game loop running
    #-- maze
maze_image = pygame.image.load("assets/map_test.png").convert()  # convert for faster pixel access
maze_mask = pygame.mask.from_threshold(maze_image, (0, 0, 0), (10, 10, 10)) #convert maze png to mask
    #-- maze
    #-- velocity
v_temp1 = random.choice([-1, 1]) * velocity
v_temp2 = random.choice([-1, 1]) * velocity
    #-- velocity
    ######## initializing game ########


class Goal:

    def __init__(self, x, y, image_path):
        self.x = x # x position of goal
        self.y = y # x position of goal
        self.image = pygame.image.load(image_path).convert_alpha() # load goal image
        self.g_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    #-- goal
    #-- goal

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
        self.h_mask = pygame.mask.from_surface(self.image)

    def draw(self, surface): # display self
        surface.blit(self.image, self.rect)
    # initialize horse object

def when_bounced(horse):
    horse.velocity_x *= 1.0001
    horse.velocity_y *= 1.0001
    return horse

def move_horse(horse, goal):
    steps = 5
    step_x = horse.velocity_x / steps
    step_y = horse.velocity_y  / steps
    m_offset = (0 - int(horse.x), 0 - int(horse.y))
    for _ in range(steps):
        horse.x += step_x
        horse.y += step_y
        horse.rect.center = (horse.x, horse.y)
        if check_maze_collision(horse, m_offset):
            horse.x -= step_x
            horse.y -= step_y
            horse.rect.center = (horse.x, horse.y)
            break
        bounce_wall_b(horse, goal)
    #horse.x += horse.velocity_x
    #horse.y += horse.velocity_y  
    #horse.rect.center = (horse.x, horse.y)


def calculate_goal_offset(horse, goal): # calculate goal's location
    goal_x = int(goal.x - goal.rect.left)  # goal's x coord
    goal_y = int(goal.y - goal.rect.top)  # goal's y coord
    return goal_x, goal_y

def check_maze_collision(horse, m_offset): # check if horse collides with maze
    return horse.h_mask.overlap(maze_mask, m_offset)

def calculate_movement(horse): # horse's movement
    old_x = horse.rect.left  # old horse x position
    old_y = horse.rect.top  # old horse y position
    new_x = old_x + horse.velocity_x  # next horse x position
    new_y = old_y + horse.velocity_y  # next horse y position
    change_x = new_x - old_x  # horse x movement
    change_y = new_y - old_y  # horse y movement
    return change_x, change_y, new_x, new_y

def r_dir_change(horse): #random adjustments to horse's velocity
    horse.velocity_x *= random.uniform(0.8, 1.2)
    horse.velocity_y *= random.uniform(0.8, 1.2)

def hit_wall_reverse(change_x, change_y, horse): # reverse direction of horse if hit wall

    if abs(change_x) > abs(change_y):  # check if hit left/right
        horse.velocity_x *= -1

    if abs(change_y) > abs(change_x):  # check if hit top/bottom
        horse.velocity_y *= -1
        
    horse.rect.center = (horse.x, horse.y)


def bounce_wall_b(horse, goal):
    goal_x, goal_y = calculate_goal_offset(horse, goal)
    
    change_x, change_y, new_x, new_y = calculate_movement(horse)
    
    m_offset = (0 - new_x, 0 - new_y)
    
    if check_maze_collision(horse, m_offset):
        r_dir_change(horse)
        hit_wall_reverse(change_x, change_y, horse)

def goal_reach(g_overlap):
    goal_ofs = (goal.rect.left - horse.rect.left, goal.rect.top - horse.rect.top)
    g_overlap = horse.h_mask.overlap(goal.g_mask, goal_ofs)
    if g_overlap != None:
        print("Win!")    

#def bounce_wall_b(horse, goal):
    goal_x = int(goal.x - goal.rect.left) # goal's x coord
    goal_y = int(goal.y - goal.rect.top) # goal's y coord
    g_overlap = horse.h_mask.overlap(goal.g_mask, (goal_x, goal_y)) # checks if goal and horse ovelap
    old_x = horse.rect.left # old horse x position
    old_y = horse.rect.top # old horse y position
    new_x = old_x + horse.velocity_x # next horse x position
    new_y = old_y + horse.velocity_y # next horse y position
    change_x = new_x - old_x # horse x movement
    change_y = new_y - old_y # horse y movement
    m_offset = (0 - new_x, 0 - new_y) # offset between maze and  horse


    if horse.h_mask.overlap(maze_mask, m_offset):  # checks if horse mask overlaps maze mask
        horse.velocity_x *= random.uniform(0.8, 1.2)  # random adjustment to x
        horse.velocity_y *= random.uniform(0.8, 1.2)  # random adjustment to y

        if(abs(change_x) > abs(change_y)):        # check if hit left/right
            horse.velocity_x *= -1
        if(abs(change_y) > abs(change_x)):         #check if hit top/bottom
            horse.velocity_y *= -1

    #if g_overlap != None:
    #    print("Win!")

    next_x = int(horse.x + horse.velocity_x)
    next_y = int(horse.y + horse.velocity_y)
    maze_ofs = ()
    #m_overlap = horse.h_mask.overlap(goal.g_mask, (goal_x, goal_y))

    if maze_mask.get_at((next_x, next_y)):  
        horse.velocity_x *= random.uniform(0.85, 1.15)  # random adjustment to x
        horse.velocity_y *= random.uniform(0.85, 1.15)  # random adjustment to y

        # reverse velocity
        if maze_mask.get_at((int(horse.x), next_y)):  # hits left or right
            horse.velocity_x *= -1 
        if maze_mask.get_at((next_x, int(horse.y))):  #hits top or bottom
            horse.velocity_y *= -1  

    if g_overlap != None:
        print("Win!")
        

    ######## create horses  ########

horse1 = Horse("Horse 1", 100, 100, "assets/horse_1.png", v_temp1, v_temp2) # <-- place horse
    ######## create horses  ########

#create goal#
goal1 = Goal(120, 120, "assets/goal.png")
#create goal#

    ######## gui open ########
while running: 
    clock.tick(60) # <-- set fps 60
    move_horse(horse1, goal1)

# for loop through the event queue 
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:  #<-- Check for QUIT event   
            running = False

    screen.blit(maze_image, (0, 0))  # <-- draw maze map
    horse1.draw(screen)  # <-- draw horses here (if any)
    goal1.draw(screen) # <- draw goal

    pygame.display.flip()  # <-- refresh screen
    ######## gui open ########
    