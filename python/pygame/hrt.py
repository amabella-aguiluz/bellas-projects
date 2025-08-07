import pygame
import os
import random
import math

    ######## initializing game ########

screen = pygame.display.set_mode((800, 600)) # set screen size (width, height)
clock = pygame.time.Clock() # set fps
velocity = 1.5 # speed of horse
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
        self.name = name
        self.x = x # starting x position
        self.y = y # starting y position
        self.velocity_x = velocity_x # velocity direction x
        self.velocity_y = velocity_y # velocity direction y
        self.image = pygame.image.load(image_path).convert_alpha() #load image
        self.rect = self.image.get_rect(center =(x, y))
        self.h_mask = pygame.mask.from_surface(self.image)

    def draw(self, surface): # display self
        surface.blit(self.image, self.rect)
    # initialize horse object

def calculate_movement(horse): # horse's movement
    old_x = horse.rect.left  # old horse x position
    old_y = horse.rect.top  # old horse y position
    new_x = old_x + horse.velocity_x  # next horse x position
    new_y = old_y + horse.velocity_y  # next horse y position
    change_x = new_x - old_x  # horse x movement
    change_y = new_y - old_y  # horse y movement
    offset = (int(horse.rect.left), int(horse.rect.top)) # offset of horse
    move_offset = (0 - (int(horse.rect.left)), 0 - int(horse.rect.top)) # offset of map vs horse
    return change_x, change_y, new_x, new_y, offset, move_offset

def when_bounced(horse):
    horse.velocity_x *= 1.0000001
    horse.velocity_y *= 1.0000001
    return horse

def move_horse(horse, goal):
    steps = int(max(abs(horse.velocity_x), abs(horse.velocity_y)) * 2) + 1
    step_x = horse.velocity_x / steps
    step_y = horse.velocity_y / steps

    for _ in range(steps):
        # Predict next position
        horse.x += step_x
        horse.y += step_y
        horse.rect.center = (horse.x, horse.y)

        move_offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))

        # If collision detected, revert and bounce
        if check_maze_collision(horse, move_offset):
            # Undo last step
            horse.x -= step_x
            horse.y -= step_y
            horse.rect.center = (horse.x, horse.y)

            bounce_wall_b(horse)
            break  # exit early on collision


# def move_horse(horse, goal):
#     change_x, change_y, new_x, new_y, offset, move_offset = calculate_movement(horse)
#     steps = 5
#     step_x = horse.velocity_x / steps
#     step_y = horse.velocity_y  / steps
#     for _ in range(steps):
#         move_offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
#         horse.x += step_x # move horse by step x
#         horse.y += step_y # move horse by step y
#         horse.rect.center = (horse.x, horse.y) # move horse rectangle to position of x and y

#         if check_maze_collision(horse, move_offset): #if detect wall
#             #horse.x -= step_x # reverse step x
#             #horse.y -= step_y # reverse step y
#             #horse.rect.center = (horse.x, horse.y) # move horse rectangle to position of x and y
#             bounce_wall_b(horse, goal, step_x, step_y) # call bounce wall
#             break
        

def calculate_goal_offset(horse, goal): # calculate goal's location
    goal_x = int(goal.x - goal.rect.left)  # goal's x coord
    goal_y = int(goal.y - goal.rect.top)  # goal's y coord
    return goal_x, goal_y

def check_maze_collision(horse, m_offset): # check if horse collides with maze
    #m_offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
    return horse.h_mask.overlap(maze_mask, m_offset)


# def r_dir_change(horse): #random adjustments to horse's velocity
#     horse.velocity_x *= random.uniform(0.8, 1.2)
#     horse.velocity_y *= random.uniform(0.8, 1.2)

def hit_wall_reverse(change_x, change_y, horse): # reverse direction of horse if hit wall
    if abs(change_x) > abs(change_y):  # check if hit left/right
        horse.velocity_x *= -1
        horse.x += horse.velocity_x

    if abs(change_y) > abs(change_x):  # check if hit top/bottom
        horse.velocity_y *= -1
        horse.y += horse.velocity_y
    else: #hit diagonal
        horse.velocity_x *= -1
        horse.velocity_y *= -1
        horse.x += horse.velocity_x
        horse.y += horse.velocity_y
        
    horse.rect.center = (horse.x, horse.y) #update rect position


def bounce_wall_b(horse):
    # Random angle deviation (in degrees)
    deviation = random.uniform(-60, 60)

    # Reverse direction
    angle = math.atan2(-horse.velocity_y, -horse.velocity_x)  # get reversed angle
    angle += math.radians(deviation)  # apply small angle deviation

    # Maintain original speed
    speed = math.hypot(horse.velocity_x, horse.velocity_y)
    horse.velocity_x = math.cos(angle) * speed
    horse.velocity_y = math.sin(angle) * speed

    # Try to push out of the wall in new direction
    max_push_attempts = 30
    push_distance = 1.0

    for _ in range(max_push_attempts):
        horse.x += horse.velocity_x * push_distance
        horse.y += horse.velocity_y * push_distance
        horse.rect.center = (horse.x, horse.y)

        offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
        if not check_maze_collision(horse, offset):
            break  # got out

    # Clamp position to screen
    horse.x = max(0, min(horse.x, 800))
    horse.y = max(0, min(horse.y, 600))
    horse.rect.center = (horse.x, horse.y)


# def bounce_wall_b(horse):
#     # Reverse direction
#     horse.velocity_x *= -1
#     horse.velocity_y *= -1


#     # Add small random change to escape stuck loop
#     horse.velocity_x *= random.uniform(0.9, 1.1)
#     horse.velocity_y *= random.uniform(0.9, 1.1)

#     # Try to push out of the wall in reversed direction
#     max_push_attempts = 30
#     push_distance = 0.5  # smaller step size for precise correction

#     for _ in range(max_push_attempts):
#         horse.x += horse.velocity_x * push_distance
#         horse.y += horse.velocity_y * push_distance
#         horse.rect.center = (horse.x, horse.y)

#         offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
#         if not check_maze_collision(horse, offset):
#             break  # successfully exited the wall

#     # Clamp position to window size
#     horse.x = max(0, min(horse.x, 800))
#     horse.y = max(0, min(horse.y, 600))
#     horse.rect.center = (horse.x, horse.y)


# def bounce_wall_b(horse):
#     # Reverse only the axis that caused the collision
#     original_x = horse.x
#     original_y = horse.y

#     # Try moving back on x-axis only
#     horse.x -= horse.velocity_x
#     horse.rect.center = (horse.x, horse.y)
#     offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
#     if check_maze_collision(horse, offset):
#         # If still colliding, reverse x
#         horse.velocity_x *= -1
#         horse.x = original_x  # reset

#     # Try moving back on y-axis only
#     horse.y -= horse.velocity_y
#     horse.rect.center = (horse.x, horse.y)
#     offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
#     if check_maze_collision(horse, offset):
#         # If still colliding, reverse y
#         horse.velocity_y *= -1
#         horse.y = original_y  # reset

#     # Final position reset
#     horse.rect.center = (horse.x, horse.y)


# def bounce_wall_b(horse):
#     # Reverse direction
#     horse.velocity_x *= -1
#     horse.velocity_y *= -1

#     # Slightly randomize to prevent repeat path
#     #r_dir_change(horse)

#     # Try to move out of wall incrementally
#     for _ in range(10):
#         horse.x += horse.velocity_x * 0.1
#         horse.y += horse.velocity_y * 0.1
#         horse.rect.center = (horse.x, horse.y)

#         offset = (int(horse.rect.left), int(horse.rect.top))
#         if not check_maze_collision(horse, offset):
#             break

#     # Clamp to screen
#     horse.x = max(0, min(horse.x, 800))
#     horse.y = max(0, min(horse.y, 600))
#     horse.rect.center = (horse.x, horse.y)


# def bounce_wall_b(horse, goal, stepx, stepy):
#     r_dir_change(horse)
#     hit_wall_reverse(stepx, stepy, horse)

#     # Push the horse out of the wall incrementally
#     max_push_attempts = 10
#     for _ in range(max_push_attempts):
#         move_offset = (0 - int(horse.rect.left), 0 - int(horse.rect.top))
#         if not check_maze_collision(horse, move_offset):
#             break  # no longer colliding
#         # Move the horse slightly in the new velocity direction
#         horse.x += horse.velocity_x * 0.1
#         horse.y += horse.velocity_y * 0.1

#     # Clamp to screen boundaries (replace 800, 600 with your actual window size)
#         horse.x = max(0, min(horse.x, 800))
#         horse.y = max(0, min(horse.y, 600))


#         horse.rect.center = (horse.x, horse.y)


def goal_reach(g_overlap):
    goal_ofs = (goal.rect.left - horse.rect.left, goal.rect.top - horse.rect.top)
    g_overlap = horse.h_mask.overlap(goal.g_mask, goal_ofs)
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
    