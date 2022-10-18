import pygame

WINDOW_TITLE = 'Tibia 2 in Python'

DISPLAY_WIDTH, DISPLAY_HEIGHT = 1800, 900
SCALE = 6.2
RENDERING_WIDTH, RENDERING_HEIGHT = DISPLAY_WIDTH / SCALE, DISPLAY_HEIGHT / SCALE
HALF_RENDERING_WIDTH, HALF_RENDERING_HEIGHT = RENDERING_WIDTH // 2, RENDERING_HEIGHT // 2

# SCALE = 2
FPS = 30
TILESIZE = 64
DEBUG = True
COLLISION_RANGE = TILESIZE

RESOURCES_ROOT = 'data'

GLOBAL_COOLDOWN = 500


class Init:
    screen = None

    def __init__(self):
        pass


if not Init.screen:
    pygame.init()
    Init.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
# screen = Init.screen
