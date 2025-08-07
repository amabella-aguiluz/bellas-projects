import pygame
import os
import random
import math
# global maze_rect
# global maze_mask

    ######## initializing game ########

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # set screen size (width, height)
clock = pygame.time.Clock() # set fps
velocity = 1.5 # speed of horse
running = True # keep game loop running
    #-- maze
maze_image = pygame.image.load("assets/map_test.png").convert_alpha()  # convert for faster pixel access
maze_rect = maze_image.get_rect()
def create_wall_mask(surface):
    mask = pygame.Mask(surface.get_size())
    surface.lock()
    for y in range(surface.get_height()):
        for x in range(surface.get_width()):
            r, g, b, a = surface.get_at((x, y))
            if r < 20 and g < 20 and b < 20 and a > 200:  # Detect black walls
                mask.set_at((x, y), 1)
    surface.unlock()
    return mask

maze_mask = create_wall_mask(maze_image)

# maze_mask.invert()
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


    def move(self, maze_rect, maze_mask):
        steps = int(max(abs(self.velocity_x), abs(self.velocity_y)) * 2) + 1
        step_x = self.velocity_x / steps
        step_y = self.velocity_y / steps

        for _ in range(steps):
            self.x += step_x
            self.y += step_y
            self.rect.center = (self.x, self.y)

            offset = (int(self.rect.x - maze_rect.left), int(self.rect.y - maze_rect.top))
            collision = maze_mask.overlap(self.h_mask, offset)

            if collision:
                # Generate a new random angle (in radians)
                angle = random.uniform(0, 2 * math.pi)
                
                # Keep the same speed magnitude
                speed = math.hypot(self.velocity_x, self.velocity_y)
                
                # New direction
                self.velocity_x = math.cos(angle) * speed
                self.velocity_y = math.sin(angle) * speed

                # Move slightly in the new direction to avoid getting stuck
                self.x += self.velocity_x
                self.y += self.velocity_y
                self.rect.center = (self.x, self.y)
                break  # Stop after bounce


        # Clamp to screen bounds
        self.x = max(0, min(self.x, SCREEN_WIDTH))
        self.y = max(0, min(self.y, SCREEN_HEIGHT))
        self.rect.center = (self.x, self.y)

    def bounce_velocity(self):
        angle = math.atan2(self.velocity_y, self.velocity_x)
        deviation = random.uniform(-math.pi / 3, math.pi / 3)  # ±60 degrees
        new_angle = angle + math.pi + deviation  # Reverse + random

        speed = math.hypot(self.velocity_x, self.velocity_y)
        self.velocity_x = math.cos(new_angle) * speed
        self.velocity_y = math.sin(new_angle) * speed



    def check_maze_collision(self, maze_rect, maze_mask):
        offset = (int(self.rect.left - maze_rect.left), int(self.rect.top - maze_rect.top))
        # offset_x = int(self.rect.left - maze_rect.left)
        # offset_y = int(self.rect.top - maze_rect.top)
        # offset = (offset_x, offset_y)
        return self.h_mask.overlap(maze_mask, offset)

    


    def bounce_off_walls(self, maze_rect, maze_mask):
        # Randomize bounce direction (±60°)
        angle = math.atan2(self.velocity_y, self.velocity_x)
        deviation = random.uniform(-math.pi / 3, math.pi / 3)  # ±60 degrees
        new_angle = angle + math.pi + deviation  # Reflect + randomize

        # Keep the original speed
        speed = math.hypot(self.velocity_x, self.velocity_y)
        self.velocity_x = math.cos(new_angle) * speed
        self.velocity_y = math.sin(new_angle) * speed

        # Try to move slightly away from the wall
        for _ in range(10):
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.x = max(0, min(self.x, SCREEN_WIDTH))
            self.y = max(0, min(self.y, SCREEN_HEIGHT))
            self.rect.center = (self.x, self.y)

            if not self.check_maze_collision(maze_rect, maze_mask):
                break  # Exit loop if out of wall



 
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


def calculate_goal_offset(horse, goal): # calculate goal's location
    goal_x = int(goal.x - goal.rect.left)  # goal's x coord
    goal_y = int(goal.y - goal.rect.top)  # goal's y coord
    return goal_x, goal_y

def goal_reach(horse, goal):
    goal_ofs = (goal.rect.left - horse.rect.left, goal.rect.top - horse.rect.top)
    g_overlap = horse.h_mask.overlap(goal.g_mask, goal_ofs)
    if g_overlap is not None:
        print(f"{horse.name} reached the goal!") 
        

    ######## create horses  ########
horses = [
    Horse("Horse 1", 100, 100, "assets/horse_1.png", v_temp1, v_temp2), # <-- place horse
    Horse("Horse 2", 130, 130, "assets/horse_2.png", v_temp1, v_temp2) # <-- place horse
]
    ######## create horses  ########

#create goal#
goal1 = Goal(300, 150, "assets/goal.png")
#create goal#

    ######## gui open ########
while running: 
    clock.tick(60) # <-- set fps 60

# for loop through the event queue 
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:  #<-- Check for QUIT event   
            running = False

    for horse in horses:
        horse.move(maze_rect, maze_mask)
        goal_reach(horse, goal1)



    screen.blit(maze_image, (0, 0))  # <-- draw maze map
    for horse in horses:
        horse.draw(screen)
        pygame.draw.rect(screen, (255, 0, 0), horse.rect, 1)  # red box around horse
        goal1.draw(screen) # <- draw goal


    pygame.draw.rect(screen, (0, 255, 0), maze_rect, 1)  # green box around maze

    pygame.display.flip()  # <-- refresh screen
    ######## gui open ########
    