import pygame
import random
import math
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

######## initializing game ########
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # set screen size (width, height)
clock = pygame.time.Clock()  # set fps
velocity = 1.5  # speed of horse
running = True  # keep game loop running

title_img = pygame.image.load("assets/title.png").convert_alpha()

# -- maze
maze_image = pygame.image.load("assets/map_test.png").convert_alpha()
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

# -- velocity
v_temp1 = random.choice([-1, 1]) * velocity
v_temp2 = random.choice([-1, 1]) * velocity
######## initializing game ########


# -- goal
class Goal:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.g_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)


# -- horse
class Horse:
    def __init__(self, name, x, y, image_path, velocity_x, velocity_y):
        self.name = name
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.h_mask = pygame.mask.from_surface(self.image)

    def draw(self, surface):
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
                # bounce in new random direction
                angle = random.uniform(0, 2 * math.pi)
                speed = math.hypot(self.velocity_x, self.velocity_y)
                self.velocity_x = math.cos(angle) * speed
                self.velocity_y = math.sin(angle) * speed
                self.x += self.velocity_x
                self.y += self.velocity_y
                self.rect.center = (self.x, self.y)
                break

        # clamp to screen
        self.x = max(0, min(self.x, SCREEN_WIDTH))
        self.y = max(0, min(self.y, SCREEN_HEIGHT))
        self.rect.center = (self.x, self.y)

    def bounce_velocity(self):
        angle = math.atan2(self.velocity_y, self.velocity_x)
        deviation = random.uniform(-math.pi / 3, math.pi / 3)  # ±60°
        new_angle = angle + math.pi + deviation
        speed = math.hypot(self.velocity_x, self.velocity_y)
        self.velocity_x = math.cos(new_angle) * speed
        self.velocity_y = math.sin(new_angle) * speed

    def check_maze_collision(self, maze_rect, maze_mask):
        offset = (int(self.rect.left - maze_rect.left), int(self.rect.top - maze_rect.top))
        return self.h_mask.overlap(maze_mask, offset)

    def bounce_off_walls(self, maze_rect, maze_mask):
        angle = math.atan2(self.velocity_y, self.velocity_x)
        deviation = random.uniform(-math.pi / 3, math.pi / 3)
        new_angle = angle + math.pi + deviation
        speed = math.hypot(self.velocity_x, self.velocity_y)
        self.velocity_x = math.cos(new_angle) * speed
        self.velocity_y = math.sin(new_angle) * speed

        for _ in range(10):
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.x = max(0, min(self.x, SCREEN_WIDTH))
            self.y = max(0, min(self.y, SCREEN_HEIGHT))
            self.rect.center = (self.x, self.y)
            if not self.check_maze_collision(maze_rect, maze_mask):
                break

    def check_other_collision(self, other):
        offset = (int(self.rect.left - other.rect.left), int(self.rect.top - other.rect.top))
        return self.h_mask.overlap(other.h_mask, offset)

    def bounce_off_other(self, other):
        angle = math.atan2(self.velocity_y, self.velocity_x)
        deviation = random.uniform(-math.pi / 3, math.pi / 3)
        new_angle = angle + math.pi + deviation
        speed = math.hypot(self.velocity_x, self.velocity_y)
        self.velocity_x = math.cos(new_angle) * speed
        self.velocity_y = math.sin(new_angle) * speed

        for _ in range(10):
            self.x += self.velocity_x
            self.y += self.velocity_y
            self.x = max(0, min(self.x, SCREEN_WIDTH))
            self.y = max(0, min(self.y, SCREEN_HEIGHT))
            self.rect.center = (self.x, self.y)
            if not self.check_other_collision(other):
                break


# -- create horses
horses = [
    Horse("Horse 1", 100, 100, "assets/horse_1.png", v_temp1, v_temp2),
    Horse("Horse 2", 130, 130, "assets/horse_2.png", v_temp1, v_temp2),
]

# -- colors
black = (0, 0, 0)
grey = (127, 127, 127)
white = (255, 255, 255)


def create_surface_with_text(text, font_size, text_rgb):
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    def __init__(self, center_position, text, font_size, text_rgb, action=None):
        self.mouse_over = False
        self.action = action

        default_image = create_surface_with_text(text, font_size, text_rgb)
        highlighted_image = create_surface_with_text(text, int(font_size * 1.2), text_rgb)

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]
        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1


# -- buttons
startg = UIElement((400, 350), "Start Game", 50, black, action=GameState.NEWGAME)
quitg = UIElement((400, 400), "Quit Game", 50, black, action=GameState.QUIT)
exitg = UIElement((400, 400), "Exit Game", 50, black, action=GameState.QUIT)

# -- goal
goal1 = Goal(300, 150, "assets/goal.png")


# -- title screen
def title(mouse_up):
    screen.blit(title_img, (0, 0))

    startg.update(pygame.mouse.get_pos(), mouse_up)
    startg.draw(screen)

    quitg.update(pygame.mouse.get_pos(), mouse_up)
    quitg.draw(screen)

    pygame.display.flip()


# -- main loop
while running:
    clock.tick(60)
    mouse_up = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_up = True

    ui_action = quitg.update(pygame.mouse.get_pos(), mouse_up)
    if ui_action is not None:
        break

    quitg.draw(screen)
    title(mouse_up)

    pygame.draw.rect(screen, (0, 255, 0), maze_rect, 1)
    pygame.display.flip()